from bsddb3 import db
import os
import sys
from subprocess import call

os.system('touch splitTerms.txt')
os.system('touch splitAds.txt')
os.system('touch splitPdates.txt')
os.system('touch splitPrices.txt')

splitTerms = open('splitTerms.txt', 'w')
splitAds = open('splitAds.txt', 'w')
splitPdates = open('splitPdates.txt', 'w')
splitPrices = open('splitPrices.txt', 'w')

termsFile = open("sortedTerms.txt")
for line in termsFile:
    line.rstrip()
    #remove backslashes
    line.replace("\\", "")
    pair = line.split(":")
    splitTerms.write(pair[0]+"\n")
    splitTerms.write(pair[1])
termsFile.close()

adsFile = open("sortedAds.txt")
for line in adsFile:
        line.rstrip()
        #remove backslashes
        line.replace("\\", "")
        pair = line.split(":")
        splitAds.write(pair[0]+"\n")
        splitAds.write(pair[1])
adsFile.close()
