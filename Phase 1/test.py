from bsddb3 import db
import bsddb3
import os
import sys
from subprocess import call

#First lets open up the necessary files
os.system('sort -u 10-terms.txt > sortedTerms.txt')
os.system('sort -u 10-ads.txt > sortedAds.txt')
os.system('sort -u 10-pdates.txt > sortedPdates.txt')
os.system('sort -u 10-prices.txt > sortedPrices.txt')

os.system('touch splitTerms.txt')
os.system('touch splitAds.txt')
os.system('touch splitPdates.txt')
os.system('touch splitPrices.txt')

splitTerms = open('splitTerms.txt', 'w')
splitAds = open('splitAds.txt', 'w')
splitPdates = open('splitPdates.txt', 'w')
splitPrices = open('splitPrices.txt', 'w')

with open('sortedTerms.txt') as termsFile:
    for line in termsFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")

        splitTerms.write(pair[0]+"\n")
        splitTerms.write(pair[1])

termsFile.close()



with open('sortedAds.txt') as adsFile:
    for line in adsFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")

        splitAds.write(pair[0]+"\n")
        splitAds.write(pair[1])

adsFile.close()

with open('sortedPdates.txt') as pDatesFile:
    for line in pDatesFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")

        splitPdates.write(pair[0]+"\n")
        splitPdates.write(pair[1])

pDatesFile.close()

with open('sortedPrices.txt') as pricesFile:
    for line in pricesFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")

        splitPrices.write(pair[0]+"\n")
        splitPrices.write(pair[1])

pricesFile.close()

#clean up files
os.system("rm -rf splitTerms.txt splitPdates.txt splitAds.txt splitPrices.txt")

database = db.DB()
database.open("ad.idx")
print(database.get(b'1003735660'))