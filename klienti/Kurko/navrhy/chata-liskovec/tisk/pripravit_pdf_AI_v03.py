from pathlib import Path
import json
import pymupdf as fitz
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, NumberObject, ArrayObject, DictionaryObject, DecodedStreamObject
ROOT=Path(__file__).resolve().parents[5]
OUT=ROOT/'klienti/Kurko/exporty/chata-liskovec'
TMP=ROOT/'tmp/pdfs'
PHOTO=ROOT/'klienti/Kurko/podklady/chata-liskovec/chata-liskovec_AI_upscale_4x.png'
SRC=OUT/'Kurko_Liskovec_2900x1100mm_PODKLAD_PRO_TISK.pdf'
MM=72/25.4
src=fitz.open(SRC)
p=src[0]
for x in p.get_images():
 if x[2:4]==(1536,1024): p.replace_image(x[0],filename=str(PHOTO))
md=src.metadata
md.update(title='KURKO - Liskovec - 2900 x 1100 mm - fotografie 4x',subject='Fotografie AI upscale Real-ESRGAN x4plus, 6144 x 4096 px. Vektorova grafika, vlozene fonty, sRGB. Profil a spadavku potvrdi tiskarna.')
src.set_metadata(md)
p.set_trimbox(p.rect);p.set_bleedbox(p.rect)
src.save(TMP/'trim.pdf',garbage=4,deflate=True)
src.close(); src=fitz.open(TMP/'trim.pdf')
w,h=src[0].rect.width,src[0].rect.height
b=10*MM; e=0.25
bleed=fitz.open(); q=bleed.new_page(width=w+2*b,height=h+2*b)
# Extend only edge strips beyond the trim; the complete original design stays at 1:1.
xs=[(0,b,0,e),(b,b+w,0,w),(b+w,w+2*b,w-e,w)]
ys=[(0,b,0,e),(b,b+h,0,h),(b+h,h+2*b,h-e,h)]
for i,(x0,x1,sx0,sx1) in enumerate(xs):
 for j,(y0,y1,sy0,sy1) in enumerate(ys):
  if i==1 and j==1: continue
  q.show_pdf_page(fitz.Rect(x0,y0,x1,y1),src,0,clip=fitz.Rect(sx0,sy0,sx1,sy1),keep_proportion=False)
q.show_pdf_page(fitz.Rect(b,b,b+w,b+h),src,0)
q.set_trimbox(fitz.Rect(b,b,b+w,b+h));q.set_bleedbox(q.rect)
bleed.set_metadata(md)
bleed.save(TMP/'bleed.pdf',garbage=4,deflate=True)

def tag_srgb(inp,out):
 r=PdfReader(inp); wr=PdfWriter();wr.clone_document_from_reader(r)
 icc=DecodedStreamObject();icc.set_data(Path('/System/Library/ColorSync/Profiles/sRGB Profile.icc').read_bytes());icc[NameObject('/N')]=NumberObject(3)
 ref=wr._add_object(icc);cs=ArrayObject([NameObject('/ICCBased'),ref]);seen=set()
 def resources(res):
  if res is None:return
  res=res.get_object()
  if id(res) in seen:return
  seen.add(id(res))
  colors=res.get('/ColorSpace',DictionaryObject()).get_object();colors[NameObject('/DefaultRGB')]=cs;res[NameObject('/ColorSpace')]=colors
  objects=res.get('/XObject',{}).get_object() if '/XObject' in res else {}
  objects.pop('/fzImg0',None)
  for val in objects.values():
   ob=val.get_object()
   if ob.get('/Subtype')=='/Image' and ob.get('/ColorSpace')=='/DeviceRGB':ob[NameObject('/ColorSpace')]=cs
   resources(ob.get('/Resources'))
 for page in wr.pages:resources(page.get('/Resources'))
 wr.add_metadata({'/Title':md['title'],'/Subject':md['subject'],'/Creator':'KURKO print preparation','/Trapped':'/False'})
 wr.compress_identical_objects()
 with open(out,'wb') as f:wr.write(f)

files=[]
for kind,name in [('trim','Kurko_Liskovec_2900x1100mm_TISK_AI_4x_v03.pdf'),('bleed','Kurko_Liskovec_2900x1100mm_TISK_AI_4x_v03_SPAD_10mm.pdf')]:
 out=OUT/name;tag_srgb(TMP/(kind+'.pdf'),out)
 d=fitz.open(out);pg=d[0]
 assert len(d)==1
 for t in ['ZAHRADA','S CHATOU','ZDE NA PRODEJ','kurko.cz','770 610 020']:assert t in pg.get_text()
 for f in pg.get_fonts(full=True):assert len(d.extract_font(f[0])[3])>0
 imgs=pg.get_images(full=True);assert any(x[2:4]==(6144,4096) for x in imgs)
 pg.get_pixmap(matrix=fitz.Matrix(0.25,0.25),alpha=False).save(str(OUT/(out.stem+'_NAHLED.png')))
 files.append({'file':name,'media_mm':[round(v/MM,3) for v in [pg.rect.width,pg.rect.height]],'trim_mm':[round(v/MM,3) for v in [pg.trimbox.width,pg.trimbox.height]],'photo_px':[6144,4096],'embedded_fonts':[f[3] for f in pg.get_fonts(full=True)],'bytes':out.stat().st_size})
(OUT/'KONTROLA_TISK_AI_v03.json').write_text(json.dumps(files,ensure_ascii=False,indent=2))
print(json.dumps(files,ensure_ascii=False,indent=2))
