#!/usr/bin/python3

import gzip
import shutil
import os
import sys

#slozka ve ktere se pracuje
DIRECTORY = './log'

#dekomprese souboru
def fileToUzip(filePath):
    inFile = gzip.open(filePath, 'rb')
    outFile = open(filePath[:-3], 'wb')
    shutil.copyfileobj(inFile, outFile)
    os.remove(filePath)

#dekomprese vsech souboru vcetne tech v podlsozkach
def folderUzip():
    for root, subdirs, files in os.walk(DIRECTORY):
        for fileName in files:
            inFile = os.path.join(root, fileName)
            fileToUzip(inFile)

if __name__ == "__main__":
    folderUzip()
