# GitHub-megvalósítási javaslat

Ez a célprojekt számára követhető javaslat. A duumbi-flow saját CI-je a dokumentáció- és skillcsomagot ellenőrzi; nem telepít termékfejlesztési kapukat.

## Egy szelet, egy nyilvántartás

A szelet négy dokumentuma a verziózott `docs/changes/<slice-id>/` mappában marad. A Project-tétel az intentre és a PR-ra hivatkozik.

Pilotra egy kijelölt, review-val védett szeletadatlap legyen a döntések forrása, például az `intent.md` metaadatszakasza. Tartalma: felelős, WORK-kezdés és lejárat; értékdöntés; igazolt érettség; elérhetőség; kódsors; bizonyíték és ellenőrzött commit; kapcsoló és eltávolítási határidő, ha van. A nyitott adat maradjon nyitott; ne töltsük ki fiktív döntéssel.

A Project-ben ezeket tükröző mezők adnak szűrhető nézetet. A [single-select mezők](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields) alkalmasak a diszkrét állapotokra. A WORK/RIGHT/FAST munkaszakasz a módszertan szabálya szerinti származtatott nézet; a GitHub nem számolja ki ezt a saját szabályt automatikusan. Pilotra dokumentált kézi frissítés elég; később eseményalapú szinkronizálás indokolható.

## CI és kiadás

| Pont | Javasolt ellenőrzés |
| --- | --- |
| Minden PR | Build, statikus ellenőrzés, érintett regresszió, biztonsági minimum. |
| M1-cél | Valódi kimenetet ellenőrző smoke/E2E, izoláció és korai architekturális ellenőrzés. |
| M2-cél | Releváns negatív/hibautak, jogosultság, kompatibilitás, üzemeltethetőség. |
| M3-cél | Reprezentatív mérés és kockázat által indokolt mély vizsgálat, konkrét buildhez kötve. |
| Kiadás | Friss bizonyíték, kijelölt engedély, fokozatos bekapcsolás és megállítási feltételek. |

A célprojekt Actions workflow-ja a verziózott követelményekből válasszon teszteket. Egy módosítható issue-címke ne tudjon kötelező ellenőrzést kihagyni. A `main` [branchvédelme](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) a releváns státuszellenőrzésekhez és review-hoz köthető. A zöld CI nem helyettesíti az értékdöntést.

Lejáratot egy napi, olvasó ellenőrzés jelezhet. Automatikus termékleállítást csak a célprojektben tervezett és kipróbált mechanizmus hajtson végre. A kapcsoló eltávolítása és a hotfix utóellenőrzése követhető feladat; nem maradhat puszta szóbeli ígéret.

## A csomag saját CI-je

A [Validate workflow](../.github/workflows/validate.yml) a skill-metaadatokat, helyi inline Markdown-hivatkozásokat, önálló telepíthetőségi határokat és a validátor negatív eseteit ellenőrzi. Nem értékeli a modell döntéseit, a külső URL-ek elérhetőségét vagy a módszertan termelékenységét.
