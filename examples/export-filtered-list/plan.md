# Végrehajtási terv

Forrás: [specifikáció](spec.md). **Csak terv; egy lépés sem futott le.**

| Lépés | Ellenőrzés | Állapot |
| --- | --- | --- |
| Exportpolitika és listanézet vizsgálata | Adathatár és engedélyezett mezők döntése visszakereshető. | Nyitott döntés |
| Kimenet előállítása a látható sorokból | JSON-visszaolvasás, sorrend, explicit mezőlista. | Nem indult |
| Gomb és letöltés bekötése | Valódi letöltés tartalmát ellenőrző happy-path próba. | Nem indult |
| Üres adat, különleges karakter, rejtett mező, hibaút | Releváns automatizált próbák és meglévő regressziók. | Nem indult |
| Felhasználói próba és review | Értékdöntés és kódsors rögzítése. | Nem indult |

A konkrét fájlok, parancsok és függőségek a célprojekt megvizsgálása után kerülnek ide. Új exportkönyvtár csak bizonyított szükség esetén kell.

## Helyreállítás

Az export funkció eltávolítása vagy kikapcsolása; a meglévő listázás ellenőrzése. Adatmigráció nem tervezett.

## Tényleges eredmény

Implementáció, build és tesztfutás nincs. Értékdöntés, M1 és discard/evolve/rewrite döntés még nem állítható. Következő lépés: a nyitott exportpolitika tisztázása, majd a felhatalmazott megvalósítás.
