# Szűrt lista exportálása

**Szintetikus oktatási példa.** Nincs mögötte implementáció, felhasználói jóváhagyás vagy tesztfutás.

## Cél és hatókör

A felhasználó a megnyitott feladatlista aktuálisan látható sorait JSON-fájlba szeretné menteni, hogy egy hibajelentéshez csatolhassa őket.

Egy szelet: az aktuális oldal exportja, a szűréssel és sorrenddel együtt. Nem cél az összes lap exportja, új lekérdezés, háttérfeladat, CSV vagy új jogosultsági rendszer.

## Elfogadási példa

A lista öt sorából a szűrés kettőt mutat. Export után a fájl pontosan ezt a két sort tartalmazza, a képernyő sorrendjében; csak az azonosító, cím és állapot mezővel. Rejtett sor vagy belső mező nem kerülhet bele.

## Állapot és kockázat

- Értékdöntés: nyitott; a példa nem jelent elfogadást.
- Érettség: nem igazolt; elérhetőség: nincs implementáció.
- Kockázat: adat exportálása; a célprojekt adatosztályozása és exportpolitikája még ellenőrizendő.
- Felelős, WORK-kezdés és lejárat: nincs kijelölve, mert nem indult valódi munka.

## Nyitott döntés

Engedélyezett-e a célprojektben e három mező helyi exportja? Éles megvalósítás előtt tisztázandó. A [specifikáció](spec.md) erre feltételes javaslatot ad.
