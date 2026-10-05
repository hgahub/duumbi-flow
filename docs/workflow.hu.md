# Munkafolyamat és fájlkonvenciók

A terv, a megvalósítás és az ellenőrzési bizonyíték külön dokumentum. A fájlnevek rögzítettek:

```text
docs/changes/<slice-id>/
  intent.md
  spec.md
  plan.md
  review.md
```

Ez új projektben ajánlott hely. Meglévő projekt dokumentált gyökerét kövesd; ne hozz létre párhuzamos nyilvántartást. A `slice-id` kisbetűs, kötőjeles, stabil név.

## Mit jelent a négy lépés?

- **plan → intent.md:** felhasználói probléma, kívánt eredmény, nem célok, elfogadási példák, kockázat és nyitott kérdések. A „plan” itt a szándék tisztázásának neve.
- **design → spec.md:** megfigyelhető viselkedés, határok, adat- és interfészszerződés, hibautak, ellenőrzés. A még el nem döntött megoldás javaslat marad.
- **build → plan.md:** a megvalósítás kis lépései, függőségei, ellenőrzése és helyreállítása. Kód csak a kért végrehajtási hatókörben készül. A „plan.md” tehát végrehajtási terv.
- **review → review.md:** a vizsgált verzió, megállapítások, lefutott és elmaradt ellenőrzések, javasolt döntés. Egy terv vagy checklist nem végrehajtási bizonyíték.

Kis feladatnál ezek röviden, egy munkamenetben készülhetnek. Nem kell négy átadás vagy négy jóváhagyás. Egy kijelölt dokumentum módosításához nem kell a többit újragenerálni.

## Hogyan kapcsolódnak az érettséghez?

| Fókusz | A négy dokumentum szerepe |
| --- | --- |
| WORK | A szándék és a hipotézis tisztázása, kísérleti terv, működési és felhasználói bizonyíték; kódsors. |
| RIGHT | Ugyanazon szerződés és implementáció stabilizálása; hibautak, security, migráció, review. |
| FAST | Előre rögzített célok mérése; indokolt optimalizálás; kiadási bizonyíték. |

Egy `review.md` keletkezhet bármelyik szakaszban. Egy fájl létrejötte nem léptet érettséget. A célprojekt egyetlen nyilvántartása tartalmazza az értékdöntést, az igazolt szintet és az elérhetőséget; a dokumentumok erre hivatkoznak.

## Minimális működési szabályok

1. Egy szeletnek legyen önállóan megfigyelhető eredménye.
2. A felhasználói jóváhagyást ne találd ki; a nyitott döntést jelöld.
3. M1-ben legyen legalább egy valódi eredményt vizsgáló happy-path teszt. A meglévő regressziók és alapkövetelmények végig megmaradnak.
4. A következő kapu feltételeit a kockázat és a célprojekt határozza meg. M3-ban a megfelelő mérés elég; optimalizálás nem kötelező.
5. Bizonytalan vagy veszélyes kísérlet sandboxban marad. Termékkódba csak ellenőrzött változtatások kerülnek.
6. Az adatvesztést, hozzáférési hibát és biztonsági minimumot nem lehet prototípusminőségre hivatkozva figyelmen kívül hagyni.
7. A review megállapítása javaslat; önmagában nem engedély merge-re vagy release-re.

## Kiadás utáni visszanézés

A WORK-ban elfogadott értékdöntés a továbbhaladás alapja, nem tartós üzleti érték bizonyítéka. A pilotban ellenőrizd a tényleges használhatóságot és a működés költségét is; az eredmény megtartás, javítás vagy kivezetés lehet.
