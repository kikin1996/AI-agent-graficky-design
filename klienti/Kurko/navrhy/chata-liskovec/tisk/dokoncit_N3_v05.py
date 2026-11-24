from pathlib import Path
import json
import pymupdf as fitz
from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject,NumberObject,ArrayObject,DictionaryObject,DecodedStreamObject,RectangleObject
ROOT=Path(__file__).resolve().parents[5]; OUT=ROOT/'klienti/Kurko/exporty/chata-liskovec';MM=72/25.4
r=PdfReader(ROOT/'tmp/pdfs/N3_v05_raw.pdf');w=PdfWriter();w.clone_document_from_reader(r)
p=w.pages[0];p.trimbox=RectangleObject([10*MM,10*MM,2910*MM,1110*MM]);p.bleedbox=p.mediabox
icc=DecodedStreamObject();icc.set_data(Path('/System/Library/ColorSync/Profiles/sRGB Profile.icc').read_bytes());icc[NameObject('/N')]=NumberObject(3)
cs=ArrayObject([NameObject('/ICCBased'),w._add_object(icc)]);seen=set()
def tag(res):
 if res is None:return
 res=res.get_object()
 if id(res) in seen:return
 seen.add(id(res))
 cols=res.get('/ColorSpace',DictionaryObject()).get_object();cols[NameObject('/DefaultRGB')]=cs;res[NameObject('/ColorSpace')]=cols
 for val in res.get('/XObject',{}).values():
  o=val.get_object()
  if o.get('/Subtype')=='/Image' and o.get('/ColorSpace')=='/DeviceRGB':o[NameObject('/ColorSpace')]=cs
  tag(o.get('/Resources'))
tag(p.get('/Resources'));w.compress_identical_objects()
with open(OUT/'N3.pdf','wb') as stream:w.write(stream)
d=fitz.open(OUT/'N3.pdf');pg=d[0]
assert abs(pg.trimbox.width/MM-2900)<.01 and abs(pg.trimbox.height/MM-1100)<.01
assert abs(pg.rect.width/MM-2920)<.01 and abs(pg.rect.height/MM-1120)<.01
for txt in ['ZAHRADA','S CHATOU','ZDE NA PRODEJ','kurko.cz','770 610 020']:assert txt in pg.get_text()
assert all(d.extract_font(f[0])[3] for f in pg.get_fonts(full=True))
assert len(pg.get_images(full=True))==1
assert any(i[2:4]==(8108,3104) for i in pg.get_images(full=True))
pg.get_pixmap(matrix=fitz.Matrix(.25,.25),alpha=False).save(OUT/'N3_SPADAVKA_NAHLED.png')
pg.get_pixmap(matrix=fitz.Matrix(.25,.25),clip=pg.trimbox,alpha=False).save(OUT/'N3_NAHLED.png')
pg.get_pixmap(matrix=fitz.Matrix(1,1),clip=fitz.Rect(2100*MM,1080*MM,2300*MM,1120*MM),alpha=False).save(ROOT/'tmp/pdfs/N3_spodni_okraj_detail.png')
trim=fitz.open();q=trim.new_page(width=2900*MM,height=1100*MM);q.show_pdf_page(q.rect,d,0,clip=pg.trimbox);q.set_trimbox(q.rect);q.set_bleedbox(q.rect)
trim.save(OUT/'N3_BEZ_SPADAVKY.pdf',garbage=4,deflate=True)
# Refresh the 1:1 proof using the latest photo placement.
proof=fitz.open();q=proof.new_page(width=297*MM,height=210*MM)
q.insert_text((10*MM,10*MM),'N3 v05 - test ostrosti fotografie / skutecna velikost billboardu 1:1',fontsize=11)
q.insert_text((10*MM,17*MM),'Tisk na A4 na sirku, 100 % / Skutecna velikost. Vypnout prizpusobeni strance.',fontsize=9)
q.draw_line((10*MM,23*MM),(110*MM,23*MM),width=.7)
for x in [10,110]:q.draw_line((x*MM,21*MM),(x*MM,25*MM),width=.7)
q.insert_text((114*MM,24*MM),'Kontrolni usecka: 100 mm',fontsize=8)
q.show_pdf_page(fitz.Rect(10*MM,30*MM,287*MM,200*MM),trim,0,clip=fitz.Rect(2010*MM,350*MM,2287*MM,520*MM))
proof.save(OUT/'Kurko_Liskovec_A4_TEST_OSTROSTI_1ku1.pdf',garbage=4,deflate=True)
proof[0].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).save(ROOT/'tmp/pdfs/N3_A4_v05.png')
report={'file':'N3.pdf','revision':'v05','trim_mm':[2900,1100],'bleed_mm':10,'media_mm':[2920,1120],'photo':'N3_panorama_v05_4x.png','single_continuous_image':True,'images':[[x[2],x[3]] for x in pg.get_images(full=True)],'font_embedded':True,'edge_stretching':False,'color':'sRGB ICC','bytes':(OUT/'N3.pdf').stat().st_size}
(OUT/'KONTROLA_N3_v05.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
