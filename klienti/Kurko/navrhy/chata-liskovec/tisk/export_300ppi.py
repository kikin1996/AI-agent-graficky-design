from pathlib import Path
import math,json,subprocess
import pymupdf as f
from pypdf import PdfReader
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
ROOT=Path(__file__).resolve().parents[5];OUT=ROOT/'klienti/Kurko/exporty/chata-liskovec';TMP=ROOT/'tmp/pdfs';TMP.mkdir(parents=True,exist_ok=True)
photo=ROOT/'klienti/Kurko/podklady/chata-liskovec/N3_panorama_v05_4x.png'
base=f.open(OUT/'N3.pdf');im=base[0].get_image_info()[0];a,b,c,d,_,_=im['transform']
scale=300/(im['width']*72/math.hypot(a,b));width=math.ceil(im['width']*scale);height=math.ceil(im['height']*scale);base.close()
jpg=TMP/'N3_panorama_300ppi.jpg'
if not jpg.exists():subprocess.run(['sips','-z',str(height),str(width),'-s','format','jpeg','-s','formatOptions','95',str(photo),'--out',str(jpg)],check=True)
# One-pixel overlaps avoid hairline seams. Tiles keep image dimensions compatible with PDF renderers.
xmid=width//2;ymid=height//2
tiles=[('TL',0,0,xmid+1,ymid+1),('TR',xmid,0,width-xmid,ymid+1),('BL',0,ymid,xmid+1,height-ymid),('BR',xmid,ymid,width-xmid,height-ymid)]
with Image.open(jpg) as im:
 for name,x,y,w,h in tiles:
  path=TMP/('N3_300ppi_'+name+'.jpg')
  if not path.exists():im.crop((x,y,x+w,y+h)).save(path,quality=95,subsampling=0)
  with Image.open(path) as tile:assert tile.size==(w,h)
reports=[]
for name in ['N3','N3_BEZ_ZLUTE']:
 doc=f.open(OUT/(name+'.pdf'));pg=doc[0];images=pg.get_images(full=True);assert len(images)==1
 oldxref=images[0][0];icc=doc.xref_get_key(oldxref,'ColorSpace')[1]
 temp=doc.new_page();refs=[];commands=[]
 for label,x,y,w,h in tiles:
  ix=temp.insert_image(f.Rect(0,0,w,h),filename=str(TMP/('N3_300ppi_'+label+'.jpg')))
  doc.xref_set_key(ix,'ColorSpace',icc)
  refs.append(f'/{label} {ix} 0 R')
  commands.append(f'q {w/width:.12f} 0 0 {h/height:.12f} {x/width:.12f} {1-(y+h)/height:.12f} cm /{label} Do Q')
 doc.delete_page(len(doc)-1)
 doc.update_object(oldxref,'<< /Type /XObject /Subtype /Form /FormType 1 /BBox [0 0 1 1] /Resources << /XObject << '+' '.join(refs)+' >> >> >>')
 doc.update_stream(oldxref,'\n'.join(commands).encode())
 meta=doc.metadata;meta['title']=name+' - 300 ppi - 2900 x 1100 mm';meta['subject']='Image resampled to 300 ppi, tiled for compatibility; source detail unchanged. Vector text and logo. sRGB, 10 mm bleed.';doc.set_metadata(meta)
 out=OUT/(name+'_300ppi.pdf');doc.save(out,garbage=4,deflate=True);doc.close()
 check=f.open(out);p=check[0];info=p.get_image_info();ppi=[]
 for image in info:
  a,b,c,d,_,_=image['transform'];ppi.append([image['width']*72/math.hypot(a,b),image['height']*72/math.hypot(c,d)])
 assert len(info)==4 and all(299.99<=v<=300.1 for pair in ppi for v in pair)
 assert abs(p.trimbox.width*25.4/72-2900)<.01 and abs(p.trimbox.height*25.4/72-1100)<.01
 assert all(check.extract_font(v[0])[3] for v in p.get_fonts(full=True))
 assert all(t in p.get_text() for t in ['ZAHRADA','S CHATOU','ZDE NA PRODEJ','kurko.cz','770 610 020'])
 assert all('/ICCBased' in check.xref_get_key(i[0],'ColorSpace')[1] for i in p.get_images(full=True))
 p.get_pixmap(matrix=f.Matrix(.20,.20),alpha=False).save(OUT/(name+'_300ppi_NAHLED.png'))
 clip=f.Rect(*[v*72/25.4 for v in [1430,540,1490,580]])
 p.get_pixmap(matrix=f.Matrix(150/72,150/72),clip=clip,alpha=False).save(TMP/(name+'_300ppi_stred.png'))
 reports.append({'file':out.name,'full_photo_pixels':[width,height],'tiles':4,'overlap_pixels':1,'effective_ppi_per_tile':ppi,'trim_mm':[2900,1100],'bleed_mm':10,'embedded_fonts':True,'source_detail_increased':False,'resampling':'macOS sips','image_encoding':'JPEG quality 95','color_space':'ICCBased sRGB','pdf_version':PdfReader(out).pdf_header,'bytes':out.stat().st_size});check.close()
(OUT/'KONTROLA_300ppi.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2));print(json.dumps(reports,ensure_ascii=False,indent=2))
