#!/usr/bin/python3
import os
import toGzip
import unzip
import numpy as np
from datetime import datetime

#----------------------------testovani kontroly data -------------------------------------------

def testDate():
    secondDate = datetime(2022, 9, 12)
    firstDate = datetime(2022, 10, 12)

    #12.10.2022 - 12.9.2022 = 30 dni % 30 = 0
    if toGzip.checkDate(firstDate,secondDate) != 0:
        return 1

    firstDate = datetime(2022, 11, 11)
    #11.11.2022 - 12.9.2022 = 60 dni % 30 = 0
    if toGzip.checkDate(firstDate,secondDate) != 0:
        return 1

    firstDate = datetime(2022, 11, 11)
    #11.11.2022 - 12.9.2022 = 60 dni % 30 = 0
    if toGzip.checkDate(firstDate,secondDate) != 0:
        return 1

    firstDate = datetime(2023, 5, 10)
    #11.11.2022 - 12.9.2022 = 240 dni % 30 = 0
    if toGzip.checkDate(firstDate,secondDate) != 0:
        return 1

    #dny 13.10.2022 - 10.11.2022, ktere neprobiha komprese
    days = np.arange(13, 31)
    for day in days:
        firstDate = datetime(2022, 10, day)
        if toGzip.checkDate(firstDate,secondDate) == 0:
            return 1

    days = np.arange(1, 10)
    for day in days:
        firstDate = datetime(2022, 11, day)
        if toGzip.checkDate(firstDate,secondDate) == 0:
            return 1

    return 0

#------------ testovani rekurze--------------------------------

def testRecursion():
    #prvni komprese
    toGzip.folderToGzip('./log')

    #kontrola pripon souboru, vsechny soubory musi koncit na .gz
    for root, subdirs, files in os.walk('./log'):
        for fileName in files:
            inFile = os.path.join(root, fileName)
            if inFile[-2:] != 'gz':
                return 1

    return 0

#-------- test vicenasobne komprese --------------------
def testDoubleCompresion():
    #druha komprese
    toGzip.folderToGzip('./log')

    #i pres to, ze komprese probehla podruhe, sobory musi byt komprimovany jen jednou
    for root, subdirs, files in os.walk('./log'):
        for fileName in files:
            inFile = os.path.join(root, fileName)
            if inFile[-5:] == 'gz.gz':
                return 1

    #uvedeni slozky do puvodniho stavu
    unzip.folderUzip('./log')
    return 0




#vypis vysledku testovani na stdout
if testDate() == 0:
    print("date test - Passed")
else:
    print("date test - Failed")

if testRecursion() == 0:
    print("recursion test - Passed")
else:
    print("recursion test - Failed")

if testDoubleCompresion() == 0:
    print("double compresion test - Passed")
else:
    print("double compresion test - Failed")