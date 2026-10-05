---
name: duumbi-build
description: "Specifikációhoz plan.md végrehajtási terv készítése és a felhasználó által kért megvalósítás elvégzése kis, ellenőrizhető változtatásokkal. Használd duumbi-flow build feladathoz. Tervkérésnél csak a tervet készíti el; nem helyettesít önálló review-t vagy kiadási engedélyt."
license: MIT
---

# Terv és megvalósítás

A build munkalépés terve `plan.md`. Először állapítsd meg: a felhasználó tervet, megvalósítást vagy mindkettőt kérte-e. A „csak terv” kérésnél ne módosíts termékkódot.

## Munkamenet

1. Olvasd el a kérést, a projekt szabályait, a releváns `intent.md` és `spec.md` tartalmát, a kódot és a munkaterület aktuális állapotát. Védd a meglévő felhasználói változtatásokat.
2. A [plan sablon](assets/plan.md) alapján tervezd meg a legkisebb értékelhető lépéseket, az ellenőrzést és a helyreállítást. Ha egy szükséges szerződés hiányzik, azt jelöld; ne találj ki üzleti döntést.
3. Megvalósítási megbízásnál dolgozz a projekt branching/worktree rendjében. Ne hozz létre hosszú életű WORK/RIGHT/FAST brancheket.
4. Elsőként a meglévő kódot, standard könyvtárat és natív képességeket használd. Őrizd meg a szükséges hibakezelést, biztonságot és akadálymentességet.
5. Futtasd a változás kockázatához és célzott kapujához szükséges ellenőrzéseket. A tervben külön jelöld a lefutott, sikertelen és elmaradt lépéseket. A parancs kiadása nem bizonyítja a sikeres befejezést.
6. Vesd össze az eredményt a szerződéssel. Ha a megvalósítás érdemben eltér, frissítsd a kapcsolódó dokumentumot az engedélyezett körben, vagy jelezd a döntési igényt.

## Érettségi határok

- M1 célú funkciószelethez legalább egy automatizált, valódi eredményt vizsgáló happy-path smoke/E2E teszt kell. A biztonsági minimum és a meglévő regresszióellenőrzések végig megmaradnak.
- M2-nél ellenőrizd a releváns negatív/hibautakat, hozzáféréseket, kompatibilitást és helyreállítást. A célprojekt kapui mérvadók.
- M3-nál a korábban rögzített környezetben és terheléssel mérj. Csak kimutatott hiányt optimalizálj; megfelelő eredmény mellett nincs kötelező átírás.
- Teszt- vagy mérési hiba után ne lazítsd csendben a célértéket. Biztonságos folytatás hiányában őrizd meg az állapotot, és jelezd a blokkot.
- Új buildnél az érintett bizonyítékokat frissítsd. Ismeretlen változási hatásnál szélesebb ellenőrzés kell.

A WORK végén legyen értékdöntés és indokolt discard/evolve/rewrite döntés. A fejlesztési elkészültségből ne következtess jóváhagyott érettségre vagy felhasználói kiadásra.

A feladat önmagában nem ad felhatalmazást külső üzenetküldésre, publikálásra vagy production-módosításra. Ezekhez a felhasználó megbízása és a célprojekt előírásai mérvadók. A megvalósítás végén röviden add meg a változást, ellenőrzést és fennmaradó kockázatot.
