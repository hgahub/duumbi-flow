# Az export szerződése

Forrás: [intent](intent.md). **Feltételes tervezési példa, nem elfogadott termékdöntés.**

## Megfigyelhető működés

- Az „Aktuális oldal exportálása” gomb a kattintás pillanatában látható sorok pillanatképét menti.
- UTF-8 JSON-tömb készül, elemenként kizárólag `id`, `title`, `status` mezőkkel, a látható sorrendben.
- Az üres lista kimenete `[]`. A fájlnév `tasks.json`.
- A meglévő, jogosultságszűrt listanézet adatait használjuk; nincs új hálózati lekérdezés. A teljes adatobjektum nem szerializálható válogatás nélkül.
- Letöltésindítási hiba esetén érthető hibaüzenet jelenik meg, a lista változatlan. A böngészőnek átadott letöltésből nem állítjuk, hogy a fájl lemezre mentése sikerült.

## Korlát és nyitott kérdés

A meglévő listanézet hozzáférési védelmét előbb meg kell vizsgálni. A megtekintési jog önmagában nem bizonyítja az exportálás engedélyét; az exportpolitika döntése nyitott. Nem kerülhet új adatáramlás élesbe ennek tisztázása előtt.

## Ellenőrzési példák

| Eset | Elvárt eredmény |
| --- | --- |
| Szűrt, rendezett lista | A letöltött JSON pontosan a látható sorokat és sorrendet tartalmazza. |
| Üres lista | Érvényes, üres JSON-tömb. |
| Ékezet és idézőjel a címben | Visszaolvasáskor változatlan szöveg. |
| Belső mező a lista adataiban | A fájlban nem szerepel. |
| Letöltésindítási hiba | Hibaüzenet; nincs hamis sikerjelzés. |

M1-hez a szűrt lista valódi fájlkimenetét ellenőrző automatizált smoke/E2E próba kell; az adat- és hozzáférési minimum előfeltétel. M2-höz a releváns negatív és hibautak is szükségesek.

## Teljesítmény és helyreállítás

Korai sanity check: a lista tényleges lapmérete és objektummérete korlátos-e? Ismeretlen korlátnál előbb mérés vagy explicit limit szükséges. M3 mérési célját a célprojekt eszközprofilja és UX-kerete alapján kell rögzíteni; ez a példa nem talál ki univerzális időhatárt.

Nincs adatírás vagy migráció. Hibánál az export belépési pontja kikapcsolható vagy eltávolítható, a listanézet regresszióellenőrzésével.
