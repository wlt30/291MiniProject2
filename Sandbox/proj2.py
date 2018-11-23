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
    os.system("sort -u pdate.txt > sortedPdate.txt")
    print("Sorted pdate.txt")
    os.system("sort -u terms.txt > sortedTerms.txt")
    print("Sorted terms.txt")
    

main()
