import os

target_chunk = "cloned_site/_next/static/chunks/2vs2yctr590c-.js"
backup_chunk = "cloned_site/_next/static/chunks/2vs2yctr590c-.js.bak"

# 1. Verify backup exists
if not os.path.exists(backup_chunk):
    raise RuntimeError("Backup file does not exist!")

with open(backup_chunk, "r", encoding="utf-8") as f:
    original_bundle = f.read()

with open("contact_tC_original.txt", "r", encoding="utf-8") as f:
    orig_tc = f.read()

assert orig_tc in original_bundle, "Original tC not found in backup bundle!"

# Upgraded tC implementation
upgraded_tC = """function tC({contactHandoffProgress:e,contactHandRevealProgress:t,camera:r}){
  let n=(0,s.q)("contact"),a=(0,i._)(),l=(0,P.useRef)(null),u=(0,P.useRef)(null),d=(0,P.useMemo)(()=>(0,C.Px)(0),[]),{data:c}=(0,m.Q)("handModel");
  (0,ey.j)("contact","hand",!0);
  let ms=(0,P.useRef)({curX:0,curY:0,targetHover:0,curHover:0,entranceTimer:0,lowPower:false,perfCount:0,perfStart:0,dprCapped:false});
  let prefersReducedMotion=(0,P.useMemo)(()=>{return typeof window!=="undefined"&&window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;},[]);
  (0,P.useEffect)(()=>{
    let canvas=document.querySelector("canvas");
    if(!canvas)return;
    let onLost=e=>{e.preventDefault();window.__mh3DContextLost=true;};
    let onRestored=()=>{window.__mh3DContextLost=false;};
    canvas.addEventListener("webglcontextlost",onLost,false);
    canvas.addEventListener("webglcontextrestored",onRestored,false);
    return ()=>{canvas.removeEventListener("webglcontextlost",onLost);canvas.removeEventListener("webglcontextrestored",onRestored);};
  },[]);
  let f=(0,P.useMemo)(()=>(function({contactHandoffProgress:e,contactHandRevealProgress:t}){
    let r={color:(0,C.Px)((0,C.j9)(0)),lightColor:(0,C.Px)((0,C.j9)(0x00f0ff)),lightDir:(0,C.Px)(new j.cE(12.65,2.5,-2.1)),intensity:(0,C.Px)(1.5),emissiveGain:(0,C.Px)(2.4),sweepDir:(0,C.Px)(new j.wq(1,.5)),sweepStart:(0,C.Px)(1.4),sweepEnd:(0,C.Px)(-1.7),sweepSoftness:(0,C.Px)(.25),uPulse:(0,C.Px)(1.0),uHover:(0,C.Px)(1.0),uBeamReact:(0,C.Px)(1.0)},
    n=C.U6.normalize(),a=r.lightDir.normalize(),l=(0,C.JC)((0,C.EB)(n,a),(0,C.CP)(0),(0,C.CP)(1)),o=td(e,t),s=(0,C.EB)(C.L1.sub(.5),r.sweepDir.normalize()),i=(0,C.GO)(r.sweepStart,r.sweepEnd,o),u=(0,C.nv)(i,i.add(r.sweepSoftness),s),d=l.mul(r.lightColor).mul(r.intensity).mul(u),c=ta(r.color.add(d)),m=ta(r.lightColor.mul(l).mul(r.emissiveGain).mul(u)),baseMat=new E.LM;
    baseMat.colorNode=c;baseMat.mrtNode=(0,C.HN)({output:(0,C.dc)(c,1),emissive:(0,C.dc)(m,1),normal:(0,C.dc)(n,1)});baseMat.side=j.Vs;
    let viewDir=(0,C.Px)(new j.cE(0,0,1)),nDotV=(0,C.JC)((0,C.EB)(n,viewDir),(0,C.CP)(0),(0,C.CP)(1)),fresnel=(0,C.TZ)((0,C.CP)(1.0).sub(nDotV),(0,C.CP)(2.2)),specFacet=(0,C.TZ)(l,(0,C.CP)(12.0));
    let coreColor=ta((0,C.j9)(0x020816).add(r.lightColor.mul(fresnel.mul((0,C.CP)(1.6)).add(specFacet.mul((0,C.CP)(1.8)))).mul(u))),
    coreEmissive=ta(r.lightColor.mul(fresnel.mul((0,C.CP)(2.2)).add(specFacet.mul((0,C.CP)(2.8)))).mul(r.emissiveGain).mul(r.uPulse).mul(r.uHover).mul(r.uBeamReact).mul(u)),
    coreMat=new E.LM;coreMat.colorNode=coreColor;coreMat.mrtNode=(0,C.HN)({output:(0,C.dc)(coreColor,1),emissive:(0,C.dc)(coreEmissive,1),normal:(0,C.dc)(n,1)});coreMat.side=j.Vs;
    let nucleusColor=(0,C.j9)(0x00f7ff),nucColNode=ta(nucleusColor.mul(r.uPulse.mul((0,C.CP)(2.2))).mul(u)),nucEmissNode=ta(nucleusColor.mul(r.uPulse.mul((0,C.CP)(3.6))).mul(r.uHover).mul(r.uBeamReact).mul(u)),nucleusMat=new E.LM;nucleusMat.colorNode=nucColNode;nucleusMat.mrtNode=(0,C.HN)({output:(0,C.dc)(nucColNode,1),emissive:(0,C.dc)(nucEmissNode,1),normal:(0,C.dc)(n,1)});nucleusMat.side=j.Vs;
    let ringRim=(0,C.TZ)((0,C.CP)(1.0).sub(nDotV),(0,C.CP)(1.8)),ringCol=ta(r.color.add(d).add(r.lightColor.mul(ringRim.mul((0,C.CP)(0.9))).mul(u))),ringEmiss=ta(r.lightColor.mul(l.mul(r.emissiveGain).add(ringRim.mul((0,C.CP)(2.2)))).mul(r.uHover).mul(r.uBeamReact).mul(u)),ringMat=new E.LM;ringMat.colorNode=ringCol;ringMat.mrtNode=(0,C.HN)({output:(0,C.dc)(ringCol,1),emissive:(0,C.dc)(ringEmiss,1),normal:(0,C.dc)(n,1)});ringMat.side=j.Vs;
    let satCol=ta((0,C.j9)(0xffffff).mul(u)),satEmiss=ta(r.lightColor.mul((0,C.CP)(3.2)).mul(r.uHover).mul(u)),satMat=new E.LM;satMat.colorNode=satCol;satMat.mrtNode=(0,C.HN)({output:(0,C.dc)(satCol,1),emissive:(0,C.dc)(satEmiss,1),normal:(0,C.dc)(n,1)});satMat.side=j.Vs;
    return{uniforms:r,material:baseMat,materials:{core:coreMat,nucleus:nucleusMat,ring:ringMat,sat:satMat,base:baseMat}};
  })({contactHandoffProgress:e,contactHandRevealProgress:t}),[e,t]);
  let p=(0,P.useMemo)(()=>{
    if(!c)return null;
    let root=(0,e9.f)(c.scene),count=0;
    let coreParent=root.getObjectByName("Cube.002")||root;
    let ring1=root.getObjectByName("GyroRing1"),ring2=root.getObjectByName("GyroRing2"),ring4=null,ring5=null;
    if(ring1){ring4=ring1.clone();ring4.name="GyroRing4";ring4.scale.multiplyScalar(1.36);ring4.rotation.set(0.85,0.42,-0.55);coreParent.add(ring4);}
    if(ring2){ring5=ring2.clone();ring5.name="GyroRing5";ring5.scale.multiplyScalar(1.72);ring5.rotation.set(-0.65,1.15,0.35);coreParent.add(ring5);}
    let plate=root.getObjectByName("ShieldPlate_0"),sats=[];
    if(plate){for(let sIdx=1;sIdx<=4;sIdx++){let sat=plate.clone();sat.name="Satellite_"+sIdx;sat.scale.setScalar(0.42+sIdx*0.08);coreParent.add(sat);sats.push(sat);}}
    root.traverse(child=>{if(child.isMesh){count+=1;if(child.name==="AICoreFacet"){child.material=f.materials.core;}else if(child.name==="AINucleus"){child.material=f.materials.nucleus;}else if(child.name&&child.name.indexOf("GyroRing")!==-1){child.material=f.materials.ring;}else if(child.name&&child.name.indexOf("Satellite")!==-1){child.material=f.materials.sat;}else{child.material=f.material;}child.frustumCulled=!1;child.layers.set(20);}});
    if(count===0){console.warn("[ContactHand] hand.glb has no mesh");return null;}
    return{root:root,ring4:ring4,ring5:ring5,sats:sats};
  },[c,f]);
  let h=(0,P.useMemo)(()=>{
    let target=p?(p.root||p):null;if(!target)return null;let anims=c?.animations??[];if(0===anims.length)return null;
    let mixer=new j.EV(target),action=mixer.clipAction(anims[0]);return action.setLoop(j.H8,1/0),{mixer:mixer,action:action};
  },[p,c]);
  let x=(0,P.useRef)(!1);
  let g=(0,P.useMemo)(()=>{let tex=new j.U7(new Uint16Array(192),192,1,j.Tr,j.HN);tex.magFilter=j.VV;tex.minFilter=j.VV;tex.wrapS=j.Jr;tex.wrapT=j.Jr;tex.generateMipmaps=!1;tex.needsUpdate=!0;return tex;},[]);
  (0,P.useEffect)(()=>()=>g.dispose(),[g]);
  let v=(0,P.useMemo)(()=>(function({contactHandoffProgress:e,contactHandRevealProgress:t,flowTime:d,waveTex:g}){
    let a={colorCore:(0,C.Px)((0,C.j9)(14745599)),colorB:(0,C.Px)((0,C.j9)(0x00d4ff)),colorA:(0,C.Px)((0,C.j9)(0x020718)),corePoint:(0,C.Px)(.57),intensity:(0,C.Px)(.88),opacity:(0,C.Px)(.82),vSharp:(0,C.Px)(260),rotation:(0,C.Px)(-.61),fadePower:(0,C.Px)(1.45),drift:(0,C.Px)(2.7),shimmer:(0,C.Px)(62),grainAmount:(0,C.Px)(.85),grainScale:(0,C.Px)(93),warpAmp:(0,C.Px)(.017),swirlAmp:(0,C.Px)(.002)},
    l=(0,C.uv)().sub(.5),o=(0,C.ai)(a.rotation),s=(0,C.Gg)(a.rotation),i=l.x.mul(o).sub(l.y.mul(s)),u=l.x.mul(s).add(l.y.mul(o)),dVal=td(e,t),c=(0,C.JC)(i.add(.5),(0,C.CP)(0),(0,C.CP)(1)),m=(0,C.zr)(g,(0,C.Cz)(c,.5)).r,fPos=u.sub(m.mul(a.warpAmp).mul(dVal)),pPos=i.add(m.mul(a.swirlAmp).mul(dVal)),h=(0,C.bi)(fPos.mul(fPos).mul(a.vSharp).negate()),x=(0,C.Gg)(pPos.mul(a.shimmer).add(d.mul(a.drift))).mul(.14).add(.86),uvGrain=(0,C.uv)().mul(a.grainScale),pGrain=(0,C.L7)((0,C.Gg)((0,C.EB)(uvGrain,(0,C.Cz)(12.9898,78.233))).mul(43758.5453)),vGrain=(0,C.CP)(1).add(pGrain.sub(.5).mul(a.grainAmount)),y=(0,C.CP)(.6).sub(dVal.mul(1.4)),bVal=(0,C.nv)(y,y.add((0,C.CP)(.4)),i),wVal=(0,C.TZ)(c,a.fadePower),M=h.mul(x).mul(vGrain).mul(a.intensity).mul(bVal).mul(wVal),S=(0,C.nv)((0,C.CP)(0),a.corePoint,c),jVal=(0,C.nv)(a.corePoint,(0,C.CP)(1),c),E=(0,C.GO)((0,C.GO)(a.colorA,a.colorB,S),a.colorCore,jVal).mul(M),T=M.mul(a.opacity);
    return{uniforms:a,nodes:{colorNode:E,emissiveNode:E,opacityNode:T}};
  })({contactHandoffProgress:e,contactHandRevealProgress:t,flowTime:d,waveTex:g}),[e,t,d,g]);
  let groundGlow=(0,P.useMemo)(()=>{let uv=(0,C.uv)().sub(.5),radialFalloff=(0,C.nv)((0,C.CP)(.25),(0,C.CP)(0),(0,C.EB)(uv,uv)),glowCol=(0,C.j9)(0x031838).mul(radialFalloff).mul((0,C.CP)(0.4)),glowEmiss=(0,C.j9)(0x005588).mul(radialFalloff).mul((0,C.CP)(0.35));return{colorNode:glowCol,emissiveNode:glowEmiss,opacityNode:radialFalloff.mul((0,C.CP)(0.5))};},[]);
  let b=function({enabled:e,camera:t,spriteRef:r,waveTex:n,rotation:a,contactHandoffProgress:l,contactHandRevealProgress:o}){
    let s=(0,m.Y)(),i=(0,P.useMemo)(()=>({waveSpeed:{current:.25},damping:{current:.95},impulseGain:{current:36},impulseRadius:{current:13},reach:{current:.18}}),[]),u=(0,P.useMemo)(()=>({h:new Float32Array(192),v:new Float32Array(192),quiet:!0}),[]),d=(0,P.useRef)({x:0,y:0}),c=(0,P.useRef)({cx:0,cy:0,valid:!1});
    return(0,y.f)((m,f)=>{
      if(!e||document.hidden||window.__mh3DContextLost)return;
      let p=r.current,h=Math.min(Math.max(f,1e-4),tm),x=(0,W.S)(l.value,o.value);
      if(p&&x>=.05){
        let e=s.current,r=e.x-d.current.x,n=e.y-d.current.y;
        if(Math.abs(r)>.001||Math.abs(n)>.001){
          d.current.x=e.x;d.current.y=e.y;tf.copy(t.position);tp.set(e.x,e.y,.5).unproject(t).sub(tf).normalize();p.getWorldPosition(th);
          let r=!1;if(Math.abs(tp.z)>1e-6){let e=(th.z-tf.z)/tp.z;e>0&&(tx.copy(tf).addScaledVector(tp,e),p.worldToLocal(tx),r=!0);}
          if(r){
            let e=a.value,t=Math.cos(e),r=Math.sin(e),n=tx.x*t-tx.y*r,l=tx.x*r+tx.y*t;
            if(c.current.valid){
              let e=(l-c.current.cy)/h*i.impulseGain.current;e=Math.max(-160,Math.min(160,e));let t=Math.max(i.reach.current,.001);
              if(Math.abs(e*=Math.exp(-(l*l)/(t*t)))>1e-4&&n>-.55&&n<.55){
                let t=(n+.5)*191,r=Math.max(i.impulseRadius.current,.5),a=Math.ceil(3*r),l=Math.round(t),o=e*h;
                for(let e=l-a;e<=l+a;e++){if(e<1||e>=191)continue;let n=(e-t)/r;u.v[e]+=o*Math.exp(-n*n);}
                u.quiet=!1;
              }
            }c.current.cx=n;c.current.cy=l;c.current.valid=!0;
          }else c.current.valid=!1;
        }
      }else c.current.valid=!1;
      if(u.quiet)return;
      let g=Math.max(i.waveSpeed.current,.01),maxSteps=ms.current.lowPower?2:10,P=Math.ceil(g*h/(.6*tc));
      P=Math.min(Math.max(P,1),maxSteps);
      let v=Math.min(g,.6*tc*P/h),y=h/P,C=v*v/(tc*tc),b=Math.max(i.damping.current,0),{h:w,v:M}=u,S=0;
      for(let e=0;e<P;e++){
        for(let e=1;e<191;e++){let t=w[e-1]+w[e+1]-2*w[e];M[e]+=(C*t-b*M[e])*y;}
        let e=M[0];for(let t=1;t<191;t++){let r=M[t];M[t]=r+.06*(e+M[t+1]-2*r);e=r;}
        for(let e=1;e<191;e++){let t=w[e]+M[e]*y;t>1.3?t=1.3:t<-1.3&&(t=-1.3);w[e]=t;}
        w[0]=.92*w[1];w[191]=.92*w[190];M[0]=.92*M[1];M[191]=.92*M[190];
      }
      for(let e=0;e<192;e++){let t=Math.abs(w[e]);t>S&&(S=t);}
      if(S>.85){let e=.85/S;for(let t=0;t<192;t++)w[t]*=e,M[t]*=e;S=.85;}
      S<.002&&(w.fill(0),M.fill(0),u.quiet=!0);
      let E=n.image.data;for(let e=0;e<192;e++)E[e]=j.km.toHalfFloat(w[e]);n.needsUpdate=!0;
    }),{controls:i};
  }({enabled:n,camera:r,spriteRef:u,waveTex:g,rotation:v.uniforms.rotation,contactHandoffProgress:e,contactHandRevealProgress:t});
  (0,y.f)((state,delta)=>{
    if(!n||document.hidden||window.__mh3DContextLost)return;
    let mState=ms.current;
    if(!mState.dprCapped&&state.gl&&state.gl.setPixelRatio){let maxDpr=window.innerWidth<768?1.5:2.0;if(state.gl.getPixelRatio&&state.gl.getPixelRatio()>maxDpr){state.gl.setPixelRatio(maxDpr);}mState.dprCapped=true;}
    if(mState.perfCount<90){if(mState.perfStart===0)mState.perfStart=performance.now();mState.perfCount++;if(mState.perfCount===90){let elapsed=(performance.now()-mState.perfStart)/1000;let avgFps=90/Math.max(elapsed,0.001);if(avgFps<48){mState.lowPower=true;if(state.gl&&state.gl.setPixelRatio)state.gl.setPixelRatio(1.0);console.warn("[Contact 3D] Adaptive quality: low-power mode active (FPS: "+avgFps.toFixed(1)+")");}}}
    let motionMult=prefersReducedMotion?0.25:1.0;let safeDelta=Math.min(Math.max(delta,1e-4),1/15);
    d.value+=safeDelta*motionMult;let time=d.value;
    mState.entranceTimer+=safeDelta;let ignitionBloom=prefersReducedMotion?1.0:(mState.entranceTimer<1.8?1.0+Math.sin(mState.entranceTimer/1.8*Math.PI)*0.8:1.0);
    let targetHover=(typeof window!=="undefined"&&window.__mhContactHoverTarget)?window.__mhContactHoverTarget:0;
    mState.curHover+=(targetHover-mState.curHover)*0.08;let hoverGain=1.0+mState.curHover*0.85;let ringSpeedMult=(1.0+mState.curHover*1.5)*motionMult;
    let beamSway=Math.sin(time*0.45)*0.035*motionMult;v.uniforms.rotation.value=-0.61+beamSway;
    if(u.current){u.current.rotation.z=beamSway*0.5;}
    let beamContact=1.0+0.25*Math.max(0,Math.sin(time*0.45));
    if(f.uniforms.uPulse){f.uniforms.uPulse.value=(1.0+0.28*Math.sin(time*2.2*motionMult))*ignitionBloom;}
    if(f.uniforms.uHover){f.uniforms.uHover.value=hoverGain;}
    if(f.uniforms.uBeamReact){f.uniforms.uBeamReact.value=beamContact;}
    let pointer=(typeof window!=="undefined"&&window.__mhMouse)?window.__mhMouse:{x:0,y:0};
    let isTouch=(typeof window!=="undefined")&&(("ontouchstart" in window)||(navigator.maxTouchPoints>0));
    let targetX=pointer.x,targetY=pointer.y;
    if(isTouch){targetX=Math.sin(time*0.5)*0.35;targetY=Math.cos(time*0.38)*0.22;}
    mState.curX+=(targetX-mState.curX)*0.06;mState.curY+=(targetY-mState.curY)*0.06;
    if(l.current){
      let baseRot=tu.f.rotation,basePos=tu.f.position;
      l.current.rotation.x=baseRot[0]+mState.curY*0.22*motionMult;
      l.current.rotation.z=baseRot[2]-mState.curX*0.22*motionMult;
      l.current.position.x=basePos[0]+mState.curX*0.5*motionMult;
      l.current.position.y=basePos[1]+mState.curY*0.35*motionMult;
      let wobble=.6*Math.sin(.37*time)+.3*Math.sin(.83*time+1.3)+.1*Math.sin(1.71*time+2.6);
      l.current.rotation.y=tv+wobble*ty;
    }
    if(u.current){u.current.position.x=11.2-mState.curX*0.65*motionMult;u.current.position.y=12.0-mState.curY*0.45*motionMult;}
    if(p){
      if(p.ring4){p.ring4.rotateX(safeDelta*0.45*ringSpeedMult);p.ring4.rotateZ(safeDelta*0.65*ringSpeedMult);}
      if(p.ring5){p.ring5.rotateY(safeDelta*0.38*ringSpeedMult);p.ring5.rotateZ(-safeDelta*0.32*ringSpeedMult);}
      if(p.sats&&p.sats.length){
        for(let sIdx=0;sIdx<p.sats.length;sIdx++){
          let sat=p.sats[sIdx],angle=time*(0.75+sIdx*0.32)*ringSpeedMult+(sIdx*Math.PI*0.5);
          let rx=1.9+sIdx*0.45,ry=1.4+sIdx*0.35;
          sat.position.set(Math.cos(angle)*rx,Math.sin(angle)*ry,Math.sin(angle*1.5)*0.8);
          sat.rotateX(safeDelta*2.2*ringSpeedMult);sat.rotateY(safeDelta*1.8*ringSpeedMult);
        }
      }
    }
    if(h){let handoff=e.value;!x.current&&handoff>=.58?(h.action.reset().play(),x.current=!0):x.current&&handoff<.48&&(h.action.stop(),x.current=!1),x.current&&h.mixer.update(safeDelta*motionMult);}
  });
  (0,P.useEffect)(()=>{return()=>{f.material.dispose();if(f.materials){if(f.materials.core)f.materials.core.dispose();if(f.materials.nucleus)f.materials.nucleus.dispose();if(f.materials.ring)f.materials.ring.dispose();if(f.materials.sat)f.materials.sat.dispose();}};},[f]);
  (0,P.useEffect)(()=>{if(h)return()=>{h.mixer.stopAllAction();};},[h]);
  let targetScene=p?(p.root||p):null,heroScale=tu.f.scale*1.32;
  return(0,o.jsxs)(o.Fragment,{children:[(0,o.jsxs)("group",{position:tP,scale:.36,children:[(0,o.jsx)("sprite",{ref:u,position:[11.2,12,-6.26],scale:[18.8,8.3,1],layers:20,frustumCulled:!1,renderOrder:-1,children:(0,o.jsx)("spriteNodeMaterial",{colorNode:v.nodes.colorNode,emissiveNode:v.nodes.emissiveNode,opacityNode:v.nodes.opacityNode,transparent:!0,depthWrite:!1,depthTest:!0,blending:j.tq})}),(0,o.jsx)("sprite",{position:[10,7.8,-2.4],scale:[9.5,3.2,1],layers:20,frustumCulled:!1,renderOrder:-2,children:(0,o.jsx)("spriteNodeMaterial",{colorNode:groundGlow.colorNode,emissiveNode:groundGlow.emissiveNode,opacityNode:groundGlow.opacityNode,transparent:!0,depthWrite:!1,depthTest:!0,blending:j.tq})}),targetScene&&(0,o.jsx)("group",{ref:l,position:tu.f.position,rotation:tu.f.rotation,scale:heroScale,children:(0,o.jsx)("primitive",{object:targetScene})})]}),(0,o.jsx)(ti,{contactHandoffProgress:e,contactHandRevealProgress:t,camera:r,enabled:n}),a&&tg&&(0,o.jsx)(tg,{beam:v.uniforms,hand:f.uniforms,poseRef:l,beamRef:u,ripple:b.controls})]})
}"""

# Perform replacement
new_bundle = original_bundle.replace(orig_tc, upgraded_tC)

assert len(new_bundle) != len(original_bundle), "Replacement did not alter bundle length!"

with open(target_chunk, "w", encoding="utf-8") as f:
    f.write(new_bundle)

print(f"Successfully applied upgraded contact 3D scene to {target_chunk}")
print(f"Old size: {len(original_bundle)} bytes -> New size: {len(new_bundle)} bytes")
