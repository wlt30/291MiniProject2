import os
from bsddb3 import db

def main():
    os.system("db_load -T -f splitAds.txt -t hash ad.idx")
main()
