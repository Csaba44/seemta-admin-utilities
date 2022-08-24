**Hamarabb kijött mint a SeeMTA v4**

mtalogs.txt és adminnick.txt-t szerkeszteni kell, különben nem fog működni.
Logolja a duty perceket, asegit használatot, fixeket, olajcserét, és a setarmort.
A logolt adatokat az admin.xlsx fájlba írja be a program.

Használat:

- Töltsd le a zip-et
- Mozgasd egy tetszőleges helyre a zipfájlt, és csomagold ki. Ekkor megjelenik egy seemta-admin-utils mappa.
- Lépj be a seemta admin utils-be, majd írd át az mtalogs.txt-t a MTA log mappádba (pl.: D:\mta\MTA\logs), majd az adminnick.txt-t az adminnevedre. _Erre azért van szükség, mivel a program a console.log fájl alapján dolgozik, amelyben tárolódik a be és ki dutyzás időpontja, stb._
- Indítsd el a main.exe alkalmazást, amennyiben a Windows Defender nem engedi annak elindítását, **saját felelősségedre** kikapcsolhatod. A seemta-admin-utilities nem tartalmaz semmiféle kártékony szoftvert, de amennyiben a gépeden vírus van, és kikapcsolod a vírusirtót, amely azt karanténba helyezhette azért **NEM vállalok felelősséget.**
- A program indításakor ki fogja logolni az excel file által jelenleg tartalmazott értékeket. Továbbá a program mindig logolni fogja a hírdetéseket, IC, OOC chat-et, stb. tehát mindent, amit megjelenít a console.log fájl.
- Lépj adminduty-ba.
- A program kijelzi az időpontot, amikor beléptél szolgálatba. Amennyiben fixet, asegitet, stb. commandot használsz, a program ki fogja jelezni a legalsó sorban a parancshasználat utáni parancsszámot és az excel doksit azonnal frissíti.
- Amikor kilépsz dutyból, **várd meg** amíg a program kiírja a kilépés időpontját (a programnak van 1-10 másodperces késleltetése), aztán zárd be a programot. Amennyiben re-dutyzol, szintén tanácsos ezeket a lépéseket követned.
- Amennyiben újra bedutyznál, kövesd a használati útmutató elején leírt pontokat.

A program semmilyen módon nem módosítja a GTA:SA fájljait, MTA fájljait vagy a SeeMTA fájljait. Továbbá semmiképpen se lép interakcióba semmilyen SeeMTA-hoz kötődő rendszerrel, **kizárólag** az MTA napilog fájlt vizsgálja, és követi figyelemmel. 

created by: **avi8#0758**

