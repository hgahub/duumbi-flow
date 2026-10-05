# Telepítés

A csomag az Agent Skills `SKILL.md` formátumát használja. A skillhez tartozó teljes mappát telepítsd: az `assets/`, `references/` és `agents/` fájlok is szükségesek lehetnek.

## Skills CLI

A [Skills CLI](https://github.com/vercel-labs/skills) ezt a repositoryformátumot kezeli:

```sh
npx skills@latest add hgahub/duumbi-flow
```

A telepítőben válaszd ki a kívánt skilleket és klienst. A parancs külső csomagot futtat és telepítési helyet módosít; ez kézi telepítési útmutató, nem a repo automatikus működése.

## Kézi telepítés

1. Klónozd vagy töltsd le a repót.
2. Válassz egy mappát a `skills/` alatt.
3. A teljes mappát másold az agented dokumentált skill-könyvtárába.
4. Meglévő azonos nevű skillt ne írj felül ellenőrzés nélkül.
5. Ellenőrizd, hogy a kliens felismeri a skillt és fel tudja oldani annak helyi hivatkozásait.

A repo önmagában nem állítja át az agent beállításait. A működési célkönyvtárat a projekt vagy a felhasználó határozza meg.

## Helyi fejlesztői ellenőrzés

Python 3.10 vagy újabb:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

A validátor a csomag szerkezetét, skill-metaadatait és helyi hivatkozásait ellenőrzi. A viselkedési vizsgálathoz lásd a [pilotot](pilot.hu.md).
