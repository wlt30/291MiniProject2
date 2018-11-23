import os
from bsddb3 import db

def sort():
    os.system("sort -u ads.txt > sortedAds.txt")
    print("Sorted ads.txt")
    os.system("sort -u prices.txt > sortedPrices.txt")
    print("Sorted prices.txt")
    os.system("sort -u pdate.txt > sortedPdates.txt")
    print("Sorted pdate.txt")
    os.system("sort -u terms.txt > sortedTerms.txt")
    print("Sorted terms.txt")
()

def clear_phase1():
    clean_up = ""
    while(clean_up.upper() != 'Y' and clean_up.upper() != 'N'):
        clean_up = input("Would you like to clean up text files? (Y/N): ")
    if(clean_up.upper() == 'Y'):
        print("Cleaning up text files..."+
          "Removing terms.txt"+
          "Removing pdates.txt"+
          "Removing ads.txt"+
          "Removing prices.txt")
        os.system("rm -rf terms.txt pdates.txt ads.txt prices.txt")
    else:
        print("Maintained text files")
()

def clear_phase2():
    clean_up = ""
    while(clean_up.upper() != 'Y' and clean_up.upper() != 'N'):
        clean_up = input("Would you like to clean up sorted files? (Y/N): ")
    if(clean_up.upper() == 'Y'):
        print("Cleaning up sorted files..."+
              "Removing sortedTerms.txt"+
              "Removing sortedPdates.txt"+
              "Removing sortedAds.txt"+
              "Removing sortedPrices.txt")
        os.system("rm -rf sortedTerms.txt sortedPdates.txt sortedAds.txt sortedPrices.txt")
    else:
        print("Maintained sorted files")
        
    clean_up = ""
    while(clean_up.upper() != 'Y' and clean_up.upper() != 'N'):
        clean_up = input("Would you like to clean up split files? (Y/N): ")
    if(clean_up.upper() == 'Y'):
        print("Cleaning up split files..."+
              "Removing splitTerms.txt"+
              "Removing splitPdates.txt"+
              "Removing splitAds.txt"+
              "Removing splitPrices.txt")
        os.system("rm -rf splitTerms.txt splitPdates.txt splitAds.txt splitPrices.txt")
    else:
        print("Maintained split files")
        
    clean_up = ""
    while(clean_up.upper() != 'Y' and clean_up.upper() != 'N'):
        clean_up = input("Would you like to clean up index files? (Y/N): ")
    if(clean_up.upper() == 'Y'):
        print("Cleaning up index files..."+
              "Removing te.idx"+
              "Removing ad.idx"+
              "Removing da.idx"+
              "Removing pr.idx")
        os.system("rm -rf ad.idx te.idx da.idx pr.idx")
    else:
        print("Maintained sorted files, split files, index files")
()

def load_dbs():
    os.system("db_load -T -c duplicates=1 -f splitAds.txt -t hash ad.idx")
    print("Created ad.idx")
    os.system("db_load -T -c duplicates=1 -f splitPdates.txt -t btree da.idx")
    print("Created da.idx")
    os.system("db_load -T -c duplicates=1 -f splitPrices.txt -t btree pr.idx")
    print("Created pr.idx")
    os.system("db_load -T -c duplicates=1 -f splitTerms.txt -t btree te.idx")
    print("Created te.idx")
()
