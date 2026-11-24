const fs=require('fs'),path=require('path'),PDF=require('pdfkit'),svgpdf=require('svg-to-pdfkit');
const root=path.resolve(__dirname,'../../../../..');
const at=(p)=>path.join(root,p);
const assets='klienti/Kurko/podklady/chata-liskovec/';
const panorama='data:image/png;base64,'+fs.readFileSync(at(assets+'N3_panorama_v05_4x.png')).toString('base64');
const font=process.env.KURKO_FONT || '/Users/kristiankaras/Library/Fonts/Poppins-Bold.ttf';
let logo=fs.readFileSync(at('klienti/Kurko/identity/logo/kurko-web-light.svg'),'utf8').replace(/<svg[^>]*>/,'<svg x="95" y="866" width="610" height="195" viewBox="0 0 210 67" color="#000000">');
const text=(x,y,size,fill,t)=>`<text x="${x}" y="${y}" font-family="Poppins" font-weight="700" font-size="${size}" fill="${fill}">${t}</text>`;
// Artwork is drawn across the complete bleed; no edge-strip stretching.
// One continuous left-outpainted panorama spans the entire artwork and bleed.
const art=`<rect x="-10" y="-10" width="2920" height="1120" fill="#457CBF"/>
<image x="-10" y="-10" width="2920" height="1120" preserveAspectRatio="xMidYMid slice" href="${panorama}"/>
<path d="M-10 -10H1184.68 Q1485.66 550 1194.86 1110H-10Z" fill="#457CBF" fill-opacity="0.94"/>
${text(90,210,151,'white','ZAHRADA')}${text(90,380,151,'white','S CHATOU')}${text(90,550,108,'#FFD139','ZDE NA PRODEJ')}
<circle cx="2990" cy="320" r="235" fill="#FFD139"/><circle cx="1070" cy="1210" r="350" fill="#FFD139"/>
<ellipse cx="260" cy="1190" rx="650" ry="390" fill="white"/>${logo}
<g transform="rotate(-8 980 735)"><rect x="685" y="628" width="665" height="213" rx="50" fill="none" stroke="white" stroke-width="9"/>${text(735,709,63,'white','kurko.cz')}${text(735,799,85,'white','770 610 020')}</g>`;
const svg=`<svg xmlns="http://www.w3.org/2000/svg" width="2920" height="1120" viewBox="-10 -10 2920 1120">${art}</svg>`;
fs.mkdirSync(at('tmp/pdfs'),{recursive:true});
fs.writeFileSync(at('klienti/Kurko/navrhy/chata-liskovec/tisk/N3_v05.svg'),svg);
const mm=72/25.4;
const d=new PDF({size:[2920*mm,1120*mm],margin:0,compress:true,pdfVersion:'1.7',info:{Title:'N3 - KURKO - Liskovec - v05',Subject:'2900 x 1100 mm + 10 mm bleed. One continuous left-outpainted garden panorama, enhanced 4x.'}});
d.pipe(fs.createWriteStream(at('tmp/pdfs/N3_v05_raw.pdf')));
d.save().scale(mm/0.75);
svgpdf(d,svg,0,0,{width:2920*0.75,height:1120*0.75,fontCallback:()=>font});d.restore();d.end();
