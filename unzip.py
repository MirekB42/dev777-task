import gzip
import shutil
import os
import sys

#dekomprese souboru
def fileToUzip(filePath):
    inFile = gzip.open(filePath, 'rb')
    outFile = open(filePath[:-3], 'wb')
    shutil.copyfileobj(inFile, outFile)
    os.remove(filePath)

#dekomprese vsech souboru vcetne tech v podlsozkach
def folderUzip(folder):
    for root, subdirs, files in os.walk(folder):
        for fileName in files:
            if fileName[-2:] == 'gz':
                inFile = os.path.join(root, fileName)
                fileToUzip(inFile)

