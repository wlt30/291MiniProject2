import sys
import os
import platform
import time
import phase1
import phase2
import re
from bsddb3 import db
import xml.etree.ElementTree as et

if((platform.system()) == "Windows"):
    cls = 'cls'
elif((platform.system()) == "Linux"):
    cls = 'clear'
elif((platform.system()) == "Darwin"):
    cls = 'clear'

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = input("Enter filename: ")
    phase1.phase1(input_file)
    cont = ""
    while(cont.upper() != 'Y' and cont.upper() != 'N'):
        cont = input("Would you like to continue to Phase 2? (Y/N)")
    if(cont == 'N'):
        print("Phase 1 completed\nExiting...")
        time.sleep(1)
        os.system(cls)
        sys.exit()
    
    os.system("sort -u ads.txt > sortedAds.txt")
    print("Sorted ads.txt")
    os.system("sort -u prices.txt > sortedPrices.txt")
    print("Sorted prices.txt")
    os.system("sort -u pdate.txt > sortedPdates.txt")
    print("Sorted pdate.txt")
    os.system("sort -u terms.txt > sortedTerms.txt")
    print("Sorted terms.txt")

    phase2.phase2()

    os.system("db_load -T -f splitAds.txt -t hash ad.idx")
    print("Created ad.idx")
    os.system("db_load -T -f splitPdates.txt -t btree da.idx")
    print("Created da.idx")
    os.system("db_load -T -f splitPrices.txt -t btree pr.idx")
    print("Created pr.idx")
    os.system("db_load -T -f splitTerms.txt -t btree te.idx")
    print("Created te.idx")

    cont = ""
    while(cont.upper() != 'Y' and cont.upper() != 'N'):
        cont = input("Would you like to continue to Phase 3? (Y/N): ")
    if(cont == 'N'):
        print("Phase 2 completed\nExiting...")
        time.sleep(1)
        os.system(cls)
        sys.exit()

    clean_up = ""
    while(clean_up.upper() != 'Y' and clean_up.upper() != 'N'):
        clean_up = input("Would you like to cclean up system files? (Y/N): ")
    if(clean_up == 'Y'):
        print("Cleaning up system files..."+
              "Removing splitTerms.txt"+
              "Removing splitPdates.txt"+
              "Removing splitAds.txt"+
              "Removing splitPrices.txt")
        os.system("rm -rf splitTerms.txt splitPdates.txt splitAds.txt splitPrices.txt")
        time.sleep(1)
        os.system(cls)
        sys.exit()

    print("Entering Phase 3")
main()
