# KURKO / Vizuální identita 0.3

Pracovní návrh · 24. 11. 2026 · připraveno pro plakáty, billboardy a digitální reklamu.

## Směr

Navazujeme na existující KURKO reality: modrý symbol, logo s černým názvem na bílém podkladu, Poppins a přehledné plochy. Navržený dojem je věcný, klidný a dostupný. Primární pracovní publikum: vlastníci řešící prodej a lidé hledající bydlení. Toto vymezení není výsledek výzkumu ani schválené strategické pozicování.

## Co je doložené a co navrhujeme

Doložené: dodané PNG, webová paleta a načítané fonty; podklady jsou z analýzy HTML/CSS ze dne 24. 11. 2026. Nově navržené: hierarchie reklamních formátů, stupnice písma, role barev v reklamě, styl ikon, pravidla fotografií a některé pohybové parametry. Ukázkové sdělení „Prostor pro váš další krok.“ je návrh textu, nikoli oficiální slogan.

## Části systému

- [Logo a chybějící varianty](logo/system.md)
- [Barvy a naměřené kontrasty](colors.md)
- [Typografická hierarchie](typography.md)
- [Fotografie a ilustrace](imagery.md)
- [Styl ikon](iconography/spec.md)
- [Pravidla pohybu](motion.md)
- [Ukázkové kompozice a kontrola](applications/KONTROLA.md)

## Před produkcí

Pro danou zakázku doplnit finální text, formát, fotografie a tisková data. Používat převzaté webové SVG pro světlé pozadí. Chybějící varianty nejsou vytvořené tím, že je tento dokument vypisuje. Dodané ukázky jsou koncepty, nikoli tisková PDF. Před širším nasazením potvrdit nové tvůrčí směřování s klientem.

## Metodika a zdroje

Struktura je adaptovaná pro KURKO podle [rampstackco / brand-identity](https://github.com/rampstackco/claude-skills/tree/main/skills/brand-identity), včetně jeho referencí identity-system-spec a contrast-and-accessibility. Nepřebíráme automaticky všechny obecné požadavky, například čitelnost celého horizontálního loga v 16 px. Není to instalace původního skillu ani redesign loga.

Fakta o klientovi: https://www.kurko.cz/ a https://www.kurko.cz/dist/generated.css; archivované HTML/CSS v ../podklady/web/. Výpočty kontrastu: sRGB linearizace s prahem 0,04045, relativní luminance a poměr (Lvyšší + 0,05)/(Lnižší + 0,05). Strojový výsledek: contrast.json. Odkaz na pravidla W3C je v colors.md.

## Závazná korekce uživatele

Žádné tmavé pozadí. Hlavní plocha je bílá, doplňkové plochy světle šedé, modrá slouží jako akcent. Platí pro všechny formáty i panel pod logem. Přítomnost tmavé proměnné v CSS nebyla důkazem, že ji web používá jako hlavní pozadí.
