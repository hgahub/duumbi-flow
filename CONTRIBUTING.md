# Hozzájárulás

A dokumentáció magyar, a fájl- és skillnevek angol, kisbetűs, kötőjeles neveket használnak.

Egy változtatás oldjon meg egy tényleges problémát. Skilljavításhoz mutass reprodukálható kérést és elvárt viselkedést. Ne adj általános szabályt egyetlen különleges eset miatt.

- A skill csak saját mappáján belüli erőforrástól függjön.
- Tartsd meg a felhasználói hatókört és a bizonyítékok korlátait.
- Új publikálási, telepítési vagy külső üzenetküldési automatizmus külön döntést igényel.
- Valós ügyféladat, titok vagy személyes környezetútvonal ne kerüljön a repóba.
- Futtasd a [fejlesztői ellenőrzést](docs/installation.hu.md).
- Commit előtt: `pre-commit run --all-files`. A commit üzenete a `.gitmessage` mintát kövesse.

A PR röviden írja le a problémát, a változást és az ellenőrzést. Ha a viselkedési teszt nem futott, jelezd. Külső forrásból átvett anyagnál őrizd meg a szükséges licencet és megjelölést.
