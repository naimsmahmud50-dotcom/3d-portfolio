const http = require('http');
const fs = require('fs');
const path = require('path');
const https = require('https');

const PORT = 3001;
const BASE_DIR = path.join(__dirname, 'cloned_site');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.ttf': 'font/ttf',
  '.wasm': 'application/wasm',
  '.mp3': 'audio/mpeg',
  '.opus': 'audio/opus',
  '.wav': 'audio/wav',
  '.ktx2': 'image/ktx2',
  '.glb': 'model/gltf-binary',
  '.gltf': 'model/gltf+json',
  '.webmanifest': 'application/manifest+json',
};

function handleRequest(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', '*');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = new URL(req.url, `http://${req.headers.host}`);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  // Stub telemetry & Cloudflare RUM endpoints
  if (pathname.startsWith('/api/telemetry') || pathname.startsWith('/cdn-cgi/')) {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      if (body) {
        console.error('🚨 [CLIENT TELEMETRY / ERROR]:', body);
      }
      if (pathname.endsWith('.js')) {
        res.writeHead(200, { 'Content-Type': 'application/javascript; charset=utf-8' });
        res.end('/* noop */');
      } else {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'ok' }));
      }
    });
    return;
  }

  // Handle Next.js image optimization locally
  if (pathname === '/_next/image') {
    const imgUrl = parsedUrl.searchParams.get('url');
    if (imgUrl) {
      const decoded = decodeURIComponent(imgUrl);
      const filename = path.basename(decoded);
      const localFile = path.join(BASE_DIR, 'assets', filename);
      if (fs.existsSync(localFile)) {
        const ext = path.extname(localFile).toLowerCase();
        res.writeHead(200, { 'Content-Type': MIME_TYPES[ext] || 'image/webp' });
        fs.createReadStream(localFile).pipe(res);
        return;
      }
    }
  }

  // Handle /lite and /lite/* routes directly
  if (pathname === '/lite' || pathname.startsWith('/lite/')) {
    const litePath = path.join(BASE_DIR, 'lite');
    if (fs.existsSync(litePath)) {
      res.writeHead(200, {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'no-cache, no-store, must-revalidate'
      });
      fs.createReadStream(litePath).pipe(res);
      return;
    }
  }

  // Mirror Vercel route redirects to avoid Next.js React error #412 hydration mismatch
  if (pathname === '/about') {
    res.writeHead(307, { 'Location': '/?glide=about' });
    res.end();
    return;
  }
  if (pathname === '/projects') {
    res.writeHead(307, { 'Location': '/?glide=projects' });
    res.end();
    return;
  }
  if (pathname === '/contact') {
    res.writeHead(307, { 'Location': '/?glide=contact' });
    res.end();
    return;
  }
  if (pathname.startsWith('/projects/')) {
    res.writeHead(307, { 'Location': '/lite' });
    res.end();
    return;
  }

  // Handle root SPA page route
  if (pathname === '/' || pathname === '/index.html') {
    const indexPath = path.join(BASE_DIR, 'index.html');
    if (fs.existsSync(indexPath)) {
      res.writeHead(200, {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'no-cache, no-store, must-revalidate'
      });
      fs.createReadStream(indexPath).pipe(res);
      return;
    }
  }

  // Local file mapping
  let localPath = path.join(BASE_DIR, pathname);

  if (fs.existsSync(localPath) && fs.statSync(localPath).isDirectory()) {
    const dirIndex = path.join(localPath, 'index.html');
    if (fs.existsSync(dirIndex)) {
      localPath = dirIndex;
    }
  }

  if (fs.existsSync(localPath) && fs.statSync(localPath).isFile()) {
    const stat = fs.statSync(localPath);
    const ext = path.extname(localPath).toLowerCase();
    let contentType = MIME_TYPES[ext];
    if (!contentType) {
      if (pathname.startsWith('/api/')) {
        contentType = 'application/json; charset=utf-8';
      } else {
        // Extensionless routes like /about, /contact, /projects, /lite are HTML
        contentType = 'text/html; charset=utf-8';
      }
    }

    const rangeHeader = req.headers.range;
    if (rangeHeader && stat.size > 0 && (ext === '.opus' || ext === '.mp3' || ext === '.wav')) {
      const parts = rangeHeader.replace(/bytes=/, '').split('-');
      const start = parseInt(parts[0], 10);
      const end = parts[1] ? parseInt(parts[1], 10) : stat.size - 1;
      const chunkSize = (end - start) + 1;
      const stream = fs.createReadStream(localPath, { start, end });
      res.writeHead(206, {
        'Content-Range': `bytes ${start}-${end}/${stat.size}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': chunkSize,
        'Content-Type': contentType,
        'Cache-Control': 'no-cache, must-revalidate',
      });
      stream.pipe(res);
      return;
    }

    res.writeHead(200, {
      'Content-Type': contentType,
      'Content-Length': stat.size,
      'Accept-Ranges': 'bytes',
      'Cache-Control': 'no-cache, must-revalidate',
    });
    fs.createReadStream(localPath).pipe(res);
    return;
  }

  // Fallback: Proxy from aengel.io
  let remoteUrl = `https://aengel.io${pathname}${parsedUrl.search}`;
  if (pathname.startsWith('/assets/')) {
    remoteUrl = `https://assets.aengel.io/${pathname.replace('/assets/', '')}`;
  }

  const clientReq = https.get(remoteUrl, { headers: { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)' } }, (remoteRes) => {
    if (remoteRes.statusCode === 200 || remoteRes.statusCode === 304) {
      const ext = path.extname(pathname).toLowerCase();
      let contentType = MIME_TYPES[ext] || remoteRes.headers['content-type'];
      if (!contentType) {
        if (pathname.startsWith('/api/')) {
          contentType = 'application/json; charset=utf-8';
        } else {
          contentType = 'text/html; charset=utf-8';
        }
      }
      res.writeHead(200, { 'Content-Type': contentType });

      // Cache static assets (except dynamic query endpoints like /_next/image)
      if (!pathname.includes('image') && !parsedUrl.search) {
        try {
          const dir = path.dirname(localPath);
          if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
          const fileStream = fs.createWriteStream(localPath);
          remoteRes.pipe(fileStream);
        } catch (_) {}
      }

      remoteRes.pipe(res);
    } else {
      if (!res.headersSent) {
        res.writeHead(remoteRes.statusCode || 404);
        res.end('Not Found');
      }
    }
  });

  clientReq.on('error', () => {
    if (!res.headersSent) {
      res.writeHead(404);
      res.end('Not Found');
    }
  });
}

const PORTS = [3000, 3001];
PORTS.forEach((port) => {
  const srv = http.createServer(handleRequest);
  srv.listen(port, '0.0.0.0', () => {
    console.log(`⚡ 3D Portfolio running on 👉 http://localhost:${port}`);
  });
  srv.on('error', (err) => {
    console.warn(`Warning: Could not bind port ${port}:`, err.message);
  });
});
