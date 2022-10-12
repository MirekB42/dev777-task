import os
import sys
import gzip
import shutil

#funkce pro kompresi souboru

#funkce provadejici kompresi jednoho souboru
def fileToGzip(filePath):
    #soubor pred kompresi
    inFile = open(filePath, 'rb')
    #soubor po kompresi
    outFile = gzip.open(filePath + '.gz', 'wb')
    #kopirovani obsahu
    shutil.copyfileobj(inFile,outFile)
    #odstraneni puvodniho nekomprimovaneho souboru
    os.remove(filePath)
    
#funkce provadejici kompresi vsech souboru v slozce a jejich podslozkach
def folderToGzip(folder):
    # pomoci os.walk je ziskan list vsech souboru ve vsech slozkach
    for root, subdirs, files in os.walk(folder):
        #prochazi list souboru a provadi jejich kompresi
        for fileName in files:
            #nutne pro ziskani uplne cesty k souboru
            inFile = os.path.join(root, fileName)
            #neprovadi kompresi jiz zkomprimovanych souboru
            if inFile[-2:] != 'gz':
                fileToGzip(inFile)
