import sys
import os
import platform
import time
import phase1
import phase2
import phase3
import sysfunc
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
    if(cont.upper() == 'N'):
        print("Phase 1 completed\nExiting...")
        sysfunc.clear_phase1()
        time.sleep(1)
        os.system(cls)
        sys.exit()

    sysfunc.sort()
    phase2.phase2()
    sysfunc.load_dbs()

    cont = ""
    while(cont.upper() != 'Y' and cont.upper() != 'N'):
        cont = input("Would you like to continue to Phase 3? (Y/N): ")
    if(cont.upper() == 'N'):
        print("Phase 2 completed\nExiting...")
        sysfunc.clear_phase2()
        time.sleep(1)
        os.system(cls)
        sys.exit()

    print("Entering Phase 3")
    exiting = False
    while(1):
        phase3.phase3()
main()
