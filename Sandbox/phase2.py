from bsddb3 import db
import os
import sys
import time
from subprocess import call

def phase2():

    os.system('touch splitTerms.txt')
    os.system('touch splitAds.txt')
    os.system('touch splitPdates.txt')
    os.system('touch splitPrices.txt')

    splitTerms = open('splitTerms.txt', 'w')
    splitAds = open('splitAds.txt', 'w')
    splitPdates = open('splitPdates.txt', 'w')
    splitPrices = open('splitPrices.txt', 'w')

    try:
        termsFile = open('sortedTerms.txt')
    except:
        print("File could not be found\nExiting...")
        time.sleep(1)
        os.system(cls)
        sys.exit()
    for line in termsFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")
        splitTerms.write(pair[0]+"\n")
        splitTerms.write(pair[1])
    termsFile.close()

    try:
        adsFile = open('sortedAds.txt')
    except:
        print("File could not be found\nExiting...")
        time.sleep(1)
        os.system(cls)
        sys.exit()
    for line in adsFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")
        splitAds.write(pair[0]+"\n")
        splitAds.write(pair[1])
    adsFile.close()

    try:
        pDatesFile = open('sortedPdates.txt')
    except:
        print("File could not be found\nExiting...")
        time.sleep(1)
        os.system(cls)
        sys.exit()
    for line in pDatesFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")
        splitPdates.write(pair[0]+"\n")
        splitPdates.write(pair[1])
    pDatesFile.close()

    try:
        pricesFile = open('sortedPrices.txt')
    except:
        print("File could not be found\nExiting...")
        time.sleep(1)
        os.system(cls)
        sys.exit()
    for line in pricesFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")
        splitPrices.write(pair[0]+"\n")
        splitPrices.write(pair[1])
    pricesFile.close()

()
