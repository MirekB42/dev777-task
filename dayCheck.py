#!/usr/bin/python3

#skript spoustejici kompresi v pripade, ze ubehlo 30 dni od poledni komprese

import os
from datetime import datetime
#funkce pro kompresi
import toGzip

#cesta ke slozce s logy 
# ./log     - testovaci slozka
# /var/log  - slozka, ve ktere bude script pracovat
DIRECTORY = './log'
#referencni datum od ktereho zacina komprese kazdych 30 dni
REFERENCE_DATE = datetime(2022, 8, 13)
#datum spusteni skriptu
TODAY = datetime.now()

#rozdil data spusteni skriptu a referencniho data
dateDelta = TODAY - REFERENCE_DATE
#vezme dny a spocita zbytek po deleni 30. Pokud je nula, tak ubehlo 30 dni od posledni komprese a je treba ji provest znovu
if dateDelta.days % 30 == 0:
    toGzip.folderToGzip(DIRECTORY)


