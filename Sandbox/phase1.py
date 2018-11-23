import sys
import os
import platform
import time
import xml.etree.ElementTree as et

if((platform.system()) == "Windows"):
    cls = 'cls'
elif((platform.system()) == "Linux"):
    cls = 'clear'
elif((platform.system()) == "Darwin"):
    cls = 'clear'

def phase1(input_file):
    try:
        tree = et.parse(input_file)
    except:
        print("Invalid file\nExiting...")
        time.sleep(1)
        os.system(cls)
        sys.exit()
    root = tree.getroot()

    term_txt=[]
    pdate_txt=[]
    price_txt=[]
    ads_txt=[]
    term=""
    aid=""
    date=""
    category=""
    location=""
    price=""
    main_tag=""
    description=""
    txt_term=""
    txt_price=""
    txt_pdate=""
    txt_ads=""

    for child in root:
        for element in child:
            if element.tag =="aid":
                aid = element.text
                
            elif element.tag == "date":
                if element.text == None:
                    break
                else:
                    date = element.text
                    
            elif element.tag == "loc":
                location = element.text
                
            elif element.tag == "cat":
                category = element.text
                txt_pdate +=("%s:%s,%s,%s\n"%(date,aid,category,location))
                pdate_txt.append(txt_pdate)
                txt_pdate =""
                
            elif element.tag == "ti":
                term = element.text
                for i in element.text.split():
                    if len(i) <=2:
                        break
                    else:
                        txt_term +=  ("%s:"% i)
                        txt_term += ("%s\n"%aid)
                        term_txt.append(txt_term)
                        txt_term =""
                        
            elif element.tag == "desc":
                description = element.text
                
            elif element.tag =="price":
                price = element.text
                if element.text == None:
                    break
                else:
                    price = element.text
                    txt_price = ("%s:%s,%s,%s\n"%(price,aid,category,location))
                    price_txt.append(txt_price)
                    txt_price=""
                    
        txt_ads = ("%s:<ad><aid>%s</aid><date>%s</date><loc>%s</loc><cat>%s</cat><ti>%s</ti><desc>%s</desc><price>%s</price></ad>\n"%(aid,aid,date,location,category,term,description,price))
        if txt_ads not in ads_txt:
            ads_txt.append(txt_ads)  #Gets rid of extra line if i don't check
        txt_ads = ""

    file_term = open("terms.txt","w")
    for term in term_txt:
        file_term.write(term)
    file_term.close()

    file_pdate = open("pdate.txt","w")
    for pdate in pdate_txt:
        file_pdate.write(pdate)
    file_pdate.close()

    file_prices = open("prices.txt","w")
    for price in price_txt:
        file_prices.write(price)
    file_prices.close()

    file_ads = open("ads.txt","w")
    for ad in ads_txt:
        file_ads.write(ad)
    file_ads.close()

    print("Completed Phase 1\nCreated ads.txt, prices.txt, pdate.txt,terms.txt\n\n")
    
()
