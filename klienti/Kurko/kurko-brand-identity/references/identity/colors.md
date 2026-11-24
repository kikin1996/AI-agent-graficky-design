# KURKO / Barevný systém

Stav: pracovní pravidla, 24. 11. 2026. Základní barvy jsou doložené CSS webu; role v grafice jsou návrh.

| Token | HEX | RGB | HSL (zaokrouhleno) |
| --- | --- | --- | --- |
| brand-primary | #457CBF | 69, 124, 191 | 213.0°, 48.8%, 51.0% |
| surface-light | #FFFFFF | 255, 255, 255 | 0.0°, 0.0%, 100.0% |
| text-primary | #000000 | 0, 0, 0 | 0.0°, 0.0%, 0.0% |
| text-heading | #283237 | 40, 50, 55 | 200.0°, 15.8%, 18.6% |
| surface-muted | #E8E8E8 | 232, 232, 232 | 0.0°, 0.0%, 91.0% |

Primární modrá označuje značku a zvýraznění. Bílá a světle šedá tvoří hlavní plochy; šedá slouží k oddělení obsahu. Pro tělo textu preferovat černou nebo tmavou šedomodrou na bílé. Nepřidávat další syté barvy bez důvodu v zadání. Poměr ploch není oficiálně určen.

Webový generated.css používá pro primární barvu HSL(213, 49%, 51%). Originál loga používá #447CBF. Ponechat logo beze změny; ostatní prvky sjednotit na #457CBF.

## Spočítané kontrasty

| Text | Pozadí | Kontrast | Běžný text AA | Velký text AA |
| --- | --- | --- | --- | --- |
| #000000 | #FFFFFF | 21.000:1 | ano | ano |
| #283237 | #FFFFFF | 13.112:1 | ano | ano |
| #457CBF | #FFFFFF | 4.296:1 | ne | ano |
| #FFFFFF | #457CBF | 4.296:1 | ne | ano |
| #000000 | #457CBF | 4.888:1 | ano | ano |
| #283237 | #E8E8E8 | 10.701:1 | ano | ano |

Hodnocení používá nezaokrouhlené hodnoty. Bílá na primární modré ani modrá na bílé nesplňuje 4,5:1 pro běžný text. Používat pro velké výrazné sdělení, nikoli pro drobné kontakty. Běžný text umístit na bílou nebo světle šedou plochu. Nový tmavší odstín zatím není zaveden.

Digitální prahy: běžný text 4,5:1; velký text 3:1 (alespoň 24 CSS px běžný nebo přibližně 18,67 CSS px tučný). Nejde o záruku čitelnosti billboardu; tu ověřovat v měřítku a z pozorovací vzdálenosti. Logotyp má v tomto kritériu výjimku, přesto musí být v aplikaci rozeznatelný. Zdroj: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html

Při UI použití nesmí barva sama sdělovat chybu, úspěch nebo stav. Doplň text či ikonu. Sémantické barvy nejsou součástí tohoto reklamního systému; při zadání UI je specifikovat zvlášť. Simulace poruch barvocitu nebyla provedena.

CMYK a Pantone: nestanoveno. Doplnit podle tiskového profilu, materiálu a nátisku; nevydávat mechanický převod RGB za schválenou tiskovou barvu.

Závazný pokyn uživatele: žádné tmavé pozadí ani tmavé panely. Tmavé odstíny lze použít pro text. Původní návrh s tmavými plochami byl zrušen.
