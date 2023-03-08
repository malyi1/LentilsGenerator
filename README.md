# Generátor symetrických dat s růzými poškozeními symetrie
Tento projekt vznikl v rámci oborového projektu KIV/OPIS (ZČU) ve spolupráci s ČVUT.
_________________________________________________________

# Analýza
Veškeré dokumenty a návrhy ze kterých se vycházelo lze nalézt ve složce analysis.

Z analýzy vyplynulo, že základem bude:
- vždy dokonale symetrický objekt.
  - Ten bude vytvořen náhodným generováním bodů v levé polovině (tyto body nazýváme pracovně lentilky), které následně bdou překlopeny do poloviny pravé, čímž docílíme 100% symetričnosti.
- plátno o velikosti 200px x 200px
- čtvercové plátno + plátno s kruhovou výsečí

Na tyto vygenerované obrázky budou následně aplikovány různé typy poškození:
- Add = náhodné přidávání určitého procenta bodů
- ShiftXY = náhodný posun určitého % lentilek jak v ose x, tak i v ose y
- remove = náhodné odstranění určitého % lentilek
- Add+ShiftXY = kombinace přidání a posunu určitého % lentilek
  - tento proces je prováděn postupně tzn. nejdříve je přidáno určité % bodů (metoda Add) a následně je náhodně vybráno % bodů, které bude posunuto metodou ShiftXY
  
Veškeré poškození je aplikováno pouze na levou polovinu.
Procento poškození je udáváno dle počtu nesymetrických párů lentilek - tj. 10 lentilek na levé polovině -> 10 symetrických na pravé. Posunu-li jednu lentilku v levé části, získám tak 1 nesymetrický pár -> míra poškození bude 10%.
 
________________________________
# Generování dat (obrázků)
Pro prvotní pokusy vygenerováno:
30 instancí obrázků pro každou míru symetrie (poškození) 0, 20, 40, 60, 80, 100%, pro každou kategorii.

Kategorie:
Generováno do čtverce
- n=80, size=10px, shiftXY
- n=80, size=10px, remove
- n=80, size=10px, add
- n=80, size=10px, add + shift XY
Generováno do kruhu
- n=80, size=10px, shiftXY
- n=80, size=10px, remove
- n=80, size=10px, add
- n=80, size=10px, add + shift XY

kde n je počet lentilek v levé části a size odpovídá velikosti lentilky.
Tyto vygenerované obrázky se nachází ve složce img.

__________________
# Uživatelská příručka
viz samostatný dokument user_guide
