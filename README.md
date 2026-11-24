# N3

Grafický projekt KURKO — billboard Chata Lískovec, 2900 × 1100 mm.

Aktuální revize **v05**: jedna souvislá panoramatická fotografie s AI rozšířením zahrady doleva, bez svislého přechodu mezi fotkami a bez rozmazaného pásu ve spadávce.

## Aktuální výstupy

- [Žlutá varianta – PDF přepočítané na 300 ppi](klienti/Kurko/exporty/chata-liskovec/N3_300ppi.pdf)
- [Bílá varianta – PDF přepočítané na 300 ppi](klienti/Kurko/exporty/chata-liskovec/N3_BEZ_ZLUTE_300ppi.pdf)
- [Informace k přepočtu 300 ppi a jeho omezením](klienti/Kurko/exporty/chata-liskovec/INFORMACE_300ppi.txt)

- [Nová modrobílá varianta bez žluté – PDF](klienti/Kurko/exporty/chata-liskovec/N3_BEZ_ZLUTE.pdf)
- [Náhled varianty bez žluté](klienti/Kurko/exporty/chata-liskovec/N3_BEZ_ZLUTE_NAHLED.png)

- [Billboard – PDF s AI zvětšenou fotografií a 10mm spadávkou](klienti/Kurko/exporty/chata-liskovec/N3.pdf)
- [Náhled billboardu](klienti/Kurko/exporty/chata-liskovec/N3_NAHLED.png)
- [A4 test ostrosti v měřítku 1:1](klienti/Kurko/exporty/chata-liskovec/Kurko_Liskovec_A4_TEST_OSTROSTI_1ku1.pdf)
- [Starší porovnání AI zvětšení (v03)](klienti/Kurko/exporty/chata-liskovec/AI_upscale_porovnani_detail.png)
- [Informace pro tiskárnu](klienti/Kurko/exporty/chata-liskovec/INFORMACE_PRO_TISKARNU_N3_v05.txt)

Fotografie je rozšířená doleva pomocí ImageGen a zvětšená modelem Real-ESRGAN x4plus na 8108 × 3104 px. Levá část zahrady je dogenerovaná; jemné textury jsou AI rekonstruované. Texty a logo zůstávají vektorové. Před výrobou je potřeba potvrdit požadovaný barevný profil, spadávku a dokončení s tiskárnou. Aktuální PDF používá sRGB; nejde o certifikované PDF/X.

## Složky projektu

- `klienti/Kurko/podklady/` — fotografie a reference.
- `klienti/Kurko/navrhy/` — návrhy, editovatelné PSD/Photocraft soubory a exportní skripty.
- `klienti/Kurko/exporty/` — PDF a náhledy.
- `klienti/Kurko/identity/` — vizuální identita.
- `klienti/Kurko/kurko-brand-identity/` — pravidla značky a referenční soubory.

Výchozí pracovní postup je v [JAK_PRACOVAT.txt](JAK_PRACOVAT.txt).
