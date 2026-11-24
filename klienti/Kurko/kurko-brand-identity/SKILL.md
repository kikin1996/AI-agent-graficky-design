---
name: kurko-brand-identity
description: Používej vizuální identitu KURKO reality při tvorbě nebo úpravách plakátů, billboardů, bannerů, příspěvků a dalších grafických materiálů pro klienta Kurko (kurko.cz). Použij také při kontrole souladu návrhu se značkou; neaktivuj pro jiné klienty ani obecné realitní dotazy.
---

# Identita značky KURKO

Tvoř grafiku podle následujícího pracovního profilu. Vychází z webových HTML/CSS a dodaného loga, ověřených 24. 11. 2026; nejde o oficiální manuál. Novější podklady klienta a konkrétní zadání mají přednost. Doporučení níže nepředstavuj jako klientem schválené normy.

## Barvy a typografie

| Role | Hodnota |
| --- | --- |
| Primární modrá pro grafiku | `#457CBF` |
| Bílá | `#FFFFFF` |
| Text | `#000000` |
| Nadpisy | `#283237` |
| Světle šedé pozadí | `#E8E8E8` |

Web používá Poppins: ExtraLight 200, Light 300, SemiBold 600 a Bold 700. Běžný webový text má váhu 300, nadpisy 600. Pro hlavní sdělení plakátů a billboardů preferuj 600–700; tenké řezy nepřenášej automaticky do textu čteného z dálky. Fontové soubory nejsou součástí skillu. V původním počítači byly ověřeny soubory Poppins v Library/Fonts; při práci jinde ověř dostupnost, české znaky a licenci pro export.

## Logo

Použij [assets/kurko-web-light.svg](assets/kurko-web-light.svg): původní vektorové cesty z webu, modrý symbol a černý text (currentColor nastaven podle základního CSS loga). Poměr stran 210 : 67. Zachovej geometrii, proporce a barvy. Původní [assets/kurko-01.png](assets/kurko-01.png) je archivní varianta s bílým písmem, nepoužívej ji v nových světlých kompozicích.

**Závazné pravidlo uživatele: žádné tmavé pozadí, ani panel pod logem.** Používej bílé nebo světle šedé hlavní plochy a modré akcenty. Tmavá je povolená pro text. Nález tmavé proměnné v CSS není potvrzením jejího použití na webu.

Pracovní ochranná zóna je čtvrtina výšky loga, není oficiálně doložená. Před tiskovým exportem ověř parametry tiskárny a barevný profil.

## Kompozice podle média

- Plakát: výrazné sdělení, dominantní fotografie, stručné údaje, logo a jedna výzva k akci. Udržuj čitelnou hierarchii.
- Billboard: krátké hlavní sdělení, jeden motiv, výrazné logo a jednoduchý kontakt či `kurko.cz`. Vynech dlouhé odstavce a drobné detaily.
- Další formáty: zachovej Poppins, modrý akcent a čisté bílé či světle šedé plochy; kompozici přizpůsob zadání.

Pro konkrétní nabídku používej fotografie dané nemovitosti. Ceny, kontakty a tvrzení přebírej ze zadání nebo ověřeného zdroje; chybějící údaje označ jako zástupné. Logo a přesnou typografii vkládej do výsledné kompozice jako samostatné prvky.

## Podklady a předání

Při chybějícím briefu využij položky z [references/zadani.txt](references/zadani.txt); ptej se jen na údaje potřebné pro aktuální výstup. Koncept lze připravit s výslovně uvedenými předpoklady. Finální tiskový export přizpůsob rozměru, měřítku, spadávce, profilu a rozlišení požadovanému tiskárnou; nevydávej RGB kódy za ověřené tiskové CMYK hodnoty.

Podrobnosti o webu, zdrojích a odvozených doporučeních jsou v [references/analyza-znacky.txt](references/analyza-znacky.txt). Čti je při rozšíření profilu nebo ověřování původu pravidel. Historické cesty uvedené v analýze popisují původ dat; přenosný originál loga je v `assets/` tohoto skillu.

Pokud pracuješ v původním projektu, ukládej zakázky do `klienti/Kurko/zadani/`, rozpracované výstupy do `navrhy/` a finální soubory do `exporty/`. Jinde respektuj uživatelem zvolené umístění. Názvy mohou mít tvar `RRRR-MM-DD_Kurko_typ-popis_v01.ext`.


## Rozšířený systém identity

Při tvorbě použij [specifikaci identity](references/identity/IDENTITA.md). Zpracovává logo, barvy, písmo, fotografie, ikony a pohyb podle struktury [rampstackco / brand-identity](https://github.com/rampstackco/claude-skills/tree/main/skills/brand-identity), přizpůsobené již existující značce. Není nutné instalovat další odkazované skilly.

- Pro barvy a jejich kombinace čti [colors.md](references/identity/colors.md). Modrá #457CBF proti bílé má pouze 4,296 : 1; pro běžný text používej tmavý text na bílé nebo světle šedé. Hodnoť velikost po finálním zmenšení, ne jen na návrhovém plátně.
- Pro logo čti [logo/system.md](references/identity/logo/system.md). Rozlišuj dodané varianty od chybějících; samotný výčet neznamená, že soubory existují.
- Pro typografii čti [typography.md](references/identity/typography.md). Nový návrh používá i Regular 400; webové řezy zůstávají uvedené výše jako zjištění.
- Pro fotografie a ilustrace čti [imagery.md](references/identity/imagery.md), pro ikony [iconography/spec.md](references/identity/iconography/spec.md).
- Pouze při animovaném výstupu čti [motion.md](references/identity/motion.md).
- Ukázky a jejich omezení jsou v [applications/KONTROLA.md](references/identity/applications/KONTROLA.md). Jsou to koncepty, nikoli schválené šablony nebo oficiální slogan.

Při rozšiřování identity ověř aplikaci alespoň na formátech relevantních pro zakázku. Nový slogan, typografickou stupnici, ikonografii a pohyb označ jako návrh do potvrzení klientem. Nevynucuj redesign loga ani obecný test celého horizontálního logotypu při 16 px. Při úpravě hlavního systému v projektu synchronizuj referenční kopii v tomto skillu, aby se verze nerozcházely.


## Dřívější billboardy klienta

Pro billboardy a prodejní reklamu nejdřív přečti [reference od uživatele](references/billboardy/REFERENCE.md) a prohlédni přiložené F5 a F2. Tyto skutečné práce určují vizuální směr přesněji než naše dřívější typografické koncepty: velká fotografie, modré panely či překryvy, bílý kruhový nebo obloukový prostor pro logo, výrazné sdělení a kontakt. Modrá smí tvořit větší plochu; zákaz se týká tmavých pozadí. Žlutá z F5 je volitelný kampaňový akcent. Její přesný odstín ani fonty billboardových titulků nejsou ověřené. Historické kontakty, výměry a hranice parcel nepřenášej automaticky do nového zadání.
