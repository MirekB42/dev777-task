#!/usr/bin/python3

#skript spoustejici kompresi v pripade, ze ubehlo 30 dni od poledni komprese

import os
import sys
from datetime import datetime
#funkce pro kompresi a kontrolu data
import toGzip
#cesta ke slozce s logy 
# ./log     - testovaci slozka
# /var/log  - slozka, ve ktere bude script pracovat
DIRECTORY = './log'
#referencni datum od ktereho zacina komprese kazdych 30 dni
REFERENCE_DATE = datetime(2022, 8, 13)
#datum spusteni skriptu
TODAY = datetime.now()

#vezme dny a spocita zbytek po deleni 30. Pokud je zbytek nula, tak ubehlo 30 dni od posledni komprese a je treba ji provest znovu
if checkDate(TODAY,REFERENCE_DATE) == 0:
    #provedeni komprese
    toGzip.folderToGzip(DIRECTORY)
    sys.exit(0)

    

