#!/usr/bin/env python3
import os
import shutil
import subprocess

SRC_DIR = "/home/mahmud-hasan/Naims Project/3d portfolio/cloned_site"
EXPORT_DIR = "/tmp/user-pages-build"
REPO_URL = "https://github.com/naimsmahmud50-dotcom/naimsmahmud50-dotcom.github.io.git"

print("🚀 Preparing deployment for naimsmahmud50-dotcom.github.io...")

if os.path.exists(EXPORT_DIR):
    shutil.rmtree(EXPORT_DIR)

shutil.copytree(SRC_DIR, EXPORT_DIR)
print(f"✓ Copied static files to {EXPORT_DIR}")

# 1. Create .nojekyll so GitHub Pages serves _next directory
with open(os.path.join(EXPORT_DIR, ".nojekyll"), "w") as f:
    f.write("")
print("✓ Created .nojekyll")

# 2. Create 404.html (copy of index.html) for SPA deep linking fallback
index_path = os.path.join(EXPORT_DIR, "index.html")
shutil.copy2(index_path, os.path.join(EXPORT_DIR, "404.html"))
print("✓ Created 404.html SPA router fallback")

# 3. Create route directory structures for clean URLs (lite/, about/, projects/, contact/, legal-notice/)
routes = ["lite", "about", "projects", "contact", "legal-notice"]
for r in routes:
    extensionless = os.path.join(EXPORT_DIR, r)
    html_src = os.path.join(EXPORT_DIR, f"{r}.html")
    
    # If an extensionless file exists, remove it so we can create a directory
    if os.path.isfile(extensionless):
        os.remove(extensionless)
    
    route_dir = os.path.join(EXPORT_DIR, r)
    os.makedirs(route_dir, exist_ok=True)
    
    if os.path.exists(html_src):
        shutil.copy2(html_src, os.path.join(route_dir, "index.html"))
    else:
        shutil.copy2(index_path, os.path.join(route_dir, "index.html"))

print("✓ Created route directories with index.html (lite, about, projects, contact, legal-notice)")

# 4. Git init, commit, and push to naimsmahmud50-dotcom.github.io
print("📤 Pushing to main branch of naimsmahmud50-dotcom.github.io...")
subprocess.run(["git", "init", "-b", "main"], cwd=EXPORT_DIR, check=True)
subprocess.run(["git", "config", "user.name", "Mahmud Hasan"], cwd=EXPORT_DIR, check=True)
subprocess.run(["git", "config", "user.email", "naimsmahmud50@gmail.com"], cwd=EXPORT_DIR, check=True)
subprocess.run(["git", "add", "-A"], cwd=EXPORT_DIR, check=True)
subprocess.run(["git", "commit", "-m", "deploy: 3D interactive portfolio live on GitHub Pages root domain"], cwd=EXPORT_DIR, check=True)
subprocess.run(["git", "remote", "add", "origin", REPO_URL], cwd=EXPORT_DIR, check=True)
subprocess.run(["git", "push", "-u", "origin", "main", "--force"], cwd=EXPORT_DIR, check=True)

print("🎉 Successfully deployed to naimsmahmud50-dotcom.github.io!")
