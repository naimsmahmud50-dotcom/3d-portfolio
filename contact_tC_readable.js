function tC({
  contactHandoffProgress:e,contactHandRevealProgress:t,camera:r
}){
  let n=(0,s.q)("contact"),a=(0,i._)(),l=(0,P.useRef)(null),u=(0,P.useRef)(null),d=(0,P.useMemo)(()=>(0,C.Px)(0),[
    
  ]),{
    data:c
  }=(0,m.Q)("handModel");
  (0,ey.j)("contact","hand",!!c);
  let f=(0,P.useMemo)(()=>(function({
    contactHandoffProgress:e,contactHandRevealProgress:t
  }){
    let r={
      color:(0,C.Px)((0,C.j9)(0)),lightColor:(0,C.Px)((0,C.j9)(0x00f0ff)),lightDir:(0,C.Px)(new j.cE(12.65,2.5,-2.1)),intensity:(0,C.Px)(1.4),emissiveGain:(0,C.Px)(2.24),sweepDir:(0,C.Px)(new j.wq(1,.5)),sweepStart:(0,C.Px)(1.4),sweepEnd:(0,C.Px)(-1.7),sweepSoftness:(0,C.Px)(.25)
    },n=C.U6.normalize(),a=r.lightDir.normalize(),l=(0,C.JC)((0,C.EB)(n,a),(0,C.CP)(0),(0,C.CP)(1)),o=td(e,t),s=(0,C.EB)(C.L1.sub(.5),r.sweepDir.normalize()),i=(0,C.GO)(r.sweepStart,r.sweepEnd,o),u=(0,C.nv)(i,i.add(r.sweepSoftness),s),d=l.mul(r.lightColor).mul(r.intensity).mul(u),c=ta(r.color.add(d)),m=ta(r.lightColor.mul(l).mul(r.emissiveGain).mul(u)),f=new E.LM;
    return f.colorNode=c,f.mrtNode=(0,C.HN)({
      output:(0,C.dc)(c,1),emissive:(0,C.dc)(m,1),normal:(0,C.dc)(n,1)
    }),f.side=j.Vs,{
      uniforms:r,material:f
    }
  })({
    contactHandoffProgress:e,contactHandRevealProgress:t
  }),[
    e,t
  ]),p=(0,P.useMemo)(()=>{
    if(!c)return null;
    let e=(0,e9.f)(c.scene),t=0;
    return(e.traverse(e=>{
      e.isMesh&&(t+=1,e.material=f.material,e.frustumCulled=!1,e.layers.set(20))
    }),0===t)?(console.warn("[
      ContactHand
    ] hand.glb has no mesh — re-export from Blender with the hand mesh included."),null):e
  },[
    c,f
  ]),h=(0,P.useMemo)(()=>{
    if(!p)return null;
    let e=c?.animations??[
      
    ];
    if(0===e.length)return console.warn("[
      ContactHand
    ] hand.glb has no animation clip — re-export from Blender with the skinned mesh's action included (push the Action down to an NLA strip)."),null;
    let t=new j.EV(p),r=t.clipAction(e[
      0
    ]);
    return r.setLoop(j.H8,1/0),{
      mixer:t,action:r
    }
  },[
    p,c
  ]),x=(0,P.useRef)(!1),g=(0,P.useMemo)(()=>{
    let e;
    return(e=new j.U7(new Uint16Array(192),192,1,j.Tr,j.HN)).magFilter=j.VV,e.minFilter=j.VV,e.wrapS=j.Jr,e.wrapT=j.Jr,e.generateMipmaps=!1,e.needsUpdate=!0,e
  },[
    
  ]);
  (0,P.useEffect)(()=>()=>g.dispose(),[
    g
  ]);
  let v=(0,P.useMemo)(()=>(function({
    contactHandoffProgress:e,contactHandRevealProgress:t,flowTime:r,waveTex:n
  }){
    let a={
      colorCore:(0,C.Px)((0,C.j9)(14745599)),colorB:(0,C.Px)((0,C.j9)(0x11acff)),colorA:(0,C.Px)((0,C.j9)(661807)),corePoint:(0,C.Px)(.57),intensity:(0,C.Px)(.7),opacity:(0,C.Px)(.8),vSharp:(0,C.Px)(334),rotation:(0,C.Px)(-.61),fadePower:(0,C.Px)(1.65),drift:(0,C.Px)(2.38),shimmer:(0,C.Px)(53),grainAmount:(0,C.Px)(1),grainScale:(0,C.Px)(93),warpAmp:(0,C.Px)(.017),swirlAmp:(0,C.Px)(.002)
    },l=(0,C.uv)().sub(.5),o=(0,C.ai)(a.rotation),s=(0,C.Gg)(a.rotation),i=l.x.mul(o).sub(l.y.mul(s)),u=l.x.mul(s).add(l.y.mul(o)),d=td(e,t),c=(0,C.JC)(i.add(.5),(0,C.CP)(0),(0,C.CP)(1)),m=(0,C.zr)(n,(0,C.Cz)(c,.5)).r,f=u.sub(m.mul(a.warpAmp).mul(d)),p=i.add(m.mul(a.swirlAmp).mul(d)),h=(0,C.bi)(f.mul(f).mul(a.vSharp).negate()),x=(0,C.Gg)(p.mul(a.shimmer).add(r.mul(a.drift))).mul(.12).add(.88),g=(0,C.uv)().mul(a.grainScale),P=(0,C.L7)((0,C.Gg)((0,C.EB)(g,(0,C.Cz)(12.9898,78.233))).mul(43758.5453)),v=(0,C.CP)(1).add(P.sub(.5).mul(a.grainAmount)),y=(0,C.CP)(.6).sub(d.mul(1.4)),b=(0,C.nv)(y,y.add((0,C.CP)(.4)),i),w=(0,C.TZ)(c,a.fadePower),M=h.mul(x).mul(v).mul(a.intensity).mul(b).mul(w),S=(0,C.nv)((0,C.CP)(0),a.corePoint,c),j=(0,C.nv)(a.corePoint,(0,C.CP)(1),c),E=(0,C.GO)((0,C.GO)(a.colorA,a.colorB,S),a.colorCore,j).mul(M),T=M.mul(a.opacity);
    return{
      uniforms:a,nodes:{
        colorNode:E,emissiveNode:E,opacityNode:T
      }
    }
  })({
    contactHandoffProgress:e,contactHandRevealProgress:t,flowTime:d,waveTex:g
  }),[
    e,t,d,g
  ]),b=function({
    enabled:e,camera:t,spriteRef:r,waveTex:n,rotation:a,contactHandoffProgress:l,contactHandRevealProgress:o
  }){
    let s=(0,m.Y)(),i=(0,P.useMemo)(()=>({
      waveSpeed:{
        current:.25
      },damping:{
        current:.95
      },impulseGain:{
        current:36
      },impulseRadius:{
        current:13
      },reach:{
        current:.18
      }
    }),[
      
    ]),u=(0,P.useMemo)(()=>({
      h:new Float32Array(192),v:new Float32Array(192),quiet:!0
    }),[
      
    ]),d=(0,P.useRef)({
      x:0,y:0
    }),c=(0,P.useRef)({
      cx:0,cy:0,valid:!1
    });
    return(0,y.f)((m,f)=>{
      let p=r.current,h=Math.min(Math.max(f,1e-4),tm),x=(0,W.S)(l.value,o.value);
      if(e&&p&&x>=.05){
        let e=s.current,r=e.x-d.current.x,n=e.y-d.current.y;
        if(Math.abs(r)>.001||Math.abs(n)>.001){
          d.current.x=e.x,d.current.y=e.y,tf.copy(t.position),tp.set(e.x,e.y,.5).unproject(t).sub(tf).normalize(),p.getWorldPosition(th);
          let r=!1;
          if(Math.abs(tp.z)>1e-6){
            let e=(th.z-tf.z)/tp.z;
            e>0&&(tx.copy(tf).addScaledVector(tp,e),p.worldToLocal(tx),r=!0)
          }if(r){
            let e=a.value,t=Math.cos(e),r=Math.sin(e),n=tx.x*t-tx.y*r,l=tx.x*r+tx.y*t;
            if(c.current.valid){
              let e=(l-c.current.cy)/h*i.impulseGain.current;
              e=Math.max(-160,Math.min(160,e));
              let t=Math.max(i.reach.current,.001);
              if(Math.abs(e*=Math.exp(-(l*l)/(t*t)))>1e-4&&n>-.55&&n<.55){
                let t=(n+.5)*191,r=Math.max(i.impulseRadius.current,.5),a=Math.ceil(3*r),l=Math.round(t),o=e*h;
                for(let e=l-a;
                e<=l+a;
                e++){
                  if(e<1||e>=191)continue;
                  let n=(e-t)/r;
                  u.v[
                    e
                  ]+=o*Math.exp(-n*n)
                }u.quiet=!1
              }
            }c.current.cx=n,c.current.cy=l,c.current.valid=!0
          }else c.current.valid=!1
        }
      }else c.current.valid=!1;
      if(u.quiet)return;
      let g=Math.max(i.waveSpeed.current,.01),P=Math.ceil(g*h/(.6*tc)),v=Math.min(g,.6*tc*(P=Math.min(Math.max(P,1),10))/h),y=h/P,C=v*v/(tc*tc),b=Math.max(i.damping.current,0),{
        h:w,v:M
      }=u,S=0;
      for(let e=0;
      e<P;
      e++){
        for(let e=1;
        e<191;
        e++){
          let t=w[
            e-1
          ]+w[
            e+1
          ]-2*w[
            e
          ];
          M[
            e
          ]+=(C*t-b*M[
            e
          ])*y
        }let e=M[
          0
        ];
        for(let t=1;
        t<191;
        t++){
          let r=M[
            t
          ];
          M[
            t
          ]=r+.06*(e+M[
            t+1
          ]-2*r),e=r
        }for(let e=1;
        e<191;
        e++){
          let t=w[
            e
          ]+M[
            e
          ]*y;
          t>1.3?t=1.3:t<-1.3&&(t=-1.3),w[
            e
          ]=t
        }w[
          0
        ]=.92*w[
          1
        ],w[
          191
        ]=.92*w[
          190
        ],M[
          0
        ]=.92*M[
          1
        ],M[
          191
        ]=.92*M[
          190
        ]
      }for(let e=0;
      e<192;
      e++){
        let t=Math.abs(w[
          e
        ]);
        t>S&&(S=t)
      }if(S>.85){
        let e=.85/S;
        for(let t=0;
        t<192;
        t++)w[
          t
        ]*=e,M[
          t
        ]*=e;
        S=.85
      }S<.002&&(w.fill(0),M.fill(0),u.quiet=!0);
      let E=n.image.data;
      for(let e=0;
      e<192;
      e++)E[
        e
      ]=j.km.toHalfFloat(w[
        e
      ]);
      n.needsUpdate=!0
    }),{
      controls:i
    }
  }({
    enabled:n,camera:r,spriteRef:u,waveTex:g,rotation:v.uniforms.rotation,contactHandoffProgress:e,contactHandRevealProgress:t
  });
  return(0,y.f)((t,r)=>{
    if(!n)return;
    if(d.value+=r,l.current){
      let e=d.value,t=.6*Math.sin(.37*e)+.3*Math.sin(.83*e+1.3)+.1*Math.sin(1.71*e+2.6);
      l.current.rotation.y=tv+t*ty
    }if(!h)return;
    let a=e.value;
    !x.current&&a>=.58?(h.action.reset().play(),x.current=!0):x.current&&a<.48&&(h.action.stop(),x.current=!1),x.current&&h.mixer.update(r)
  }),(0,P.useEffect)(()=>()=>f.material.dispose(),[
    f
  ]),(0,P.useEffect)(()=>{
    if(h)return()=>{
      h.mixer.stopAllAction()
    }
  },[
    h
  ]),(0,o.jsxs)(o.Fragment,{
    children:[
      (0,o.jsxs)("group",{
        position:tP,scale:.36,children:[
          (0,o.jsx)("sprite",{
            ref:u,position:[
              11.2,12,-6.26
            ],scale:[
              18.8,8.3,1
            ],layers:20,frustumCulled:!1,renderOrder:-1,children:(0,o.jsx)("spriteNodeMaterial",{
              colorNode:v.nodes.colorNode,emissiveNode:v.nodes.emissiveNode,opacityNode:v.nodes.opacityNode,transparent:!0,depthWrite:!1,depthTest:!0,blending:j.tq
            })
          }),p&&(0,o.jsx)("group",{
            ref:l,position:tu.f.position,rotation:tu.f.rotation,scale:tu.f.scale,children:(0,o.jsx)("primitive",{
              object:p
            })
          })
        ]
      }),(0,o.jsx)(ti,{
        contactHandoffProgress:e,contactHandRevealProgress:t,camera:r,enabled:n
      }),a&&tg&&(0,o.jsx)(tg,{
        beam:v.uniforms,hand:f.uniforms,poseRef:l,beamRef:u,ripple:b.controls
      })
    ]
  })
}