
Seznam souboru a slozek:
  slozka log - testovaci slozka pouzita misto cilove /var/log  
  dayCheck.py - skript, ktery bude spousten pomoci cron  
  toGzip.py - modul s funkcemi pro kompresi dat a kontrolovani casoveho intervalu, po ktery neprobehla komprese  
  unzip - modul s pomocnymi funkcemi pro testovani. Vraci testovaci slozku ./log do puvodniho stavu  
  tests.py - program provadejici testovani  

Pridani do crontab:
  0 0 * * *  /absolutni_cesta_k_python3 /absolutni_cesta_ke_skriptu_dayCheck.py  
  Skript bude automaticky spusten kazdy den o pulnoci a komprese se provede v pripade, ze celociselny zbytek po deleni rozdilu aktualniho data a referencniho data je roven nule a tedy ubehlo 30 dni od posledni komprese. (Prvni provedeni nebude po presne 30 dnech. bylo by nutne upravit referencni datum)

testy:
  1. test kontroluje funkci pro zjisteni, zda ubehlo 30 dni od posledni komprese
  2. test kontroluje, zda jsou komprimovany soubory ve vsech podslozkach
  3. test kontroluje, zda soubory, ktere jsou jiz v .gz formatu nejsou komprimovany znovu

zaver:
  Pri reseni ve firme bych tento projekt povazoval za hotovy az po konzultaci s nadrizenym a pripadne administratorem z produkce.  
  V projektu by bylo mozne pridat vice typu komprimovnych souboru, pro ktere by komprese nebyla provadena znovu. Dale by bylo mozne pridat vice testu.