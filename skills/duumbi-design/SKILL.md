---
name: duumbi-design
description: "Fejlesztési szándékból vagy meglévő intent.md-ből spec.md kidolgozása. Használd megfigyelhető viselkedés, adat- és interfészszerződés, hibautak, kockázatok és ellenőrzési feltételek tervezésére. Nem kódmegvalósítás."
license: MIT
---

# A megoldás szerződése

A kért szelet `spec.md` dokumentumát készítsd el. Az elfogadási példákból és a tényleges rendszerből indulj ki.

## Munkamenet

1. Olvasd el az `intent.md`-t, ha létezik, a vonatkozó projektelőírásokat, a kódot és a korábbi döntéseket. Ha nincs intent, de a kérés elég pontos, dolgozz abból; ne tegyél másik skillt kötelező előfeltétellé.
2. Írd le a kívülről megfigyelhető működést, a nem célokat, a hibautakat, valamint az adat- és hozzáférési határokat.
3. Válassz a meglévő minták, natív eszközök és egyszerű megoldások közül. Új absztrakciót vagy függőséget konkrét szükséglet indokoljon.
4. Rögzítsd a kockázatot, az ellenőrzési példákat és a releváns teljesítmény/élménycélokat. Ne találj ki univerzális küszöböt.
5. Jelöld, mi eldöntött, mi javaslat és mi akadályozza a megvalósítást. Jelentős, nehezen visszafordítható döntéshez a projekt rendje szerinti döntési jegyzetet használd.
6. A kijelölt szeletmappában a [spec sablon](assets/spec.md) alapján írj vagy frissíts `spec.md`-t, majd olvasd vissza.

A szakaszok mélyülő bizonyítékot kérnek: WORK-ban működési példa és biztonsági minimum; RIGHT-ban helyesség és üzemeltethetőség; FAST-ban releváns mérések. A tesztelés folyamatos, szükséges vizsgálatot ne halassz pusztán a szakasz neve miatt.

Újraírásnál a viselkedési cél maradhat, de a régi implementáció ellenőrzése nem igazolja az új kódot. A specifikáció önmagában nem termék-, merge- vagy kiadási jóváhagyás. Kódot csak külön kért megvalósítási hatókörben módosíts.
