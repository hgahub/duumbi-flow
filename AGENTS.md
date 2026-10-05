# duumbi-flow

Ez dokumentáció- és skillcsomag, nem alkalmazás vagy agent-runtime.

- Tartsd meg a plan → intent.md, design → spec.md, build → plan.md, review → review.md megfeleltetést.
- A munkalépéseket ne azonosítsd a WORK/RIGHT/FAST fókuszokkal vagy az M1/M2/M3 érettséggel.
- A nyilvános példák legyenek szintetikusak; ne hozz át privát tudástári adatot.
- A skills/ alatti skillek legyenek önállóan telepíthetők. Külső skill vagy MCP nem kötelező függőség.
- A dokumentáció magyar. A felhasználó konkrét nyelvi és hatóköri kérését kövesd.
- Csak szükséges fájlt hozz létre. Változtatás után futtasd: python3 scripts/validate.py és python3 -m unittest discover -s tests -v.
- Skillmódosításnál a szerkezeti validáció mellett indokolt viselkedési próbát is végezz.
- Ne állíts publikálást, lefutott tesztet vagy jóváhagyást bizonyíték nélkül.
