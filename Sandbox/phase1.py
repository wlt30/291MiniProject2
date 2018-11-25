import sys
import os
import platform
import time
import re
import xml.etree.ElementTree as et

if((platform.system()) == "Windows"):
    cls = 'cls'
elif((platform.system()) == "Linux"):
    cls = 'clear'
elif((platform.system()) == "Darwin"):
    cls = 'clear'

def phase1(input_file):

    #Set variables in preparation for file creation

    ads_list = []
    date_list =[]
    price_list = []
    terms_list = []



    txt_term =""
    txt_desc =""
    txt_price =""
    txt_pdate =""
    txt_ads =""

    test=[]


    try:
        file = open(input_file, "r")
    except:
        print("Invalid file\nExiting...")
        time.sleep(1)
        os.system(cls)
        sys.exit()


    for line in file:

#Skip 1st 2 lines
        if "<ad>" in line:

#Split based on tag
#Split will return 2 indexes
#1st index  = value between tag
#2nd index = rest of add
            split_aid = line.split("<aid>")
            aid_split = split_aid[1].split("</aid>")
            aid = aid_split[0]


            split_date = aid_split[1].split("<date>")
            date_split = split_date[1].split("</date>")
            date = date_split[0]


            split_loc = date_split[1].split("<loc>")
            loc_split = split_loc[1].split("</loc>")
            loc = loc_split[0]


            split_cat = loc_split[1].split("<cat>")
            cat_split = split_cat[1].split("</cat>")
            cat = cat_split[0]


            split_ti = cat_split[1].split("<ti>")
            ti_split = split_ti[1].split("</ti>")
            ti = ti_split[0]


    #Meeting Conditions for terms.txt
            pat= re.compile(r'&#\d{0,100};')
            check_terms1 = re.sub(pat,'',ti_split[0])
            check_terms2 = re.sub('&apos;', "'", check_terms1)
            check_terms3 = re.sub('&quot;', '"', check_terms2)
            check_terms_last = re.sub('&amp;' ,'&', check_terms3)

            pattern = re.compile('[^a-zA-Z0-9_-]')
            check_terms = re.sub(pattern,' ',check_terms_last)


            for term in check_terms.split():
                if re.match(r'[0-9a-zA-Z_-]',term):
                    if len(term) <=2:
                        pass
                    else:
                        txt_term += ("%s:%s\n"%(term.lower(),aid))
                        terms_list.append(txt_term)
                        txt_term =""



            split_desc = ti_split[1].split("<desc>")
            desc_split = split_desc[1].split("</desc>")


        #Meeting Conditions for terms.txt
            pat= re.compile(r'&#\d{0,100};')
            check_terms1 = re.sub(pat,'',desc_split[0])
            check_terms2 = re.sub('&apos;', "'", check_terms1)
            check_terms3 = re.sub('&quot;', '"', check_terms2)
            check_terms_last = re.sub('&amp;', '&', check_terms3)

            pattern2 = re.compile('[^a-zA-Z0-9_-]')
            check_desc = re.sub(pattern2,' ',check_terms_last)

            for word in check_desc.split():
                if re.match(r'[0-9a-zA-Z_-]',word):
                    if len(word) <=2:
                        pass
                    else:
                        txt_desc += ("%s:%s\n"%(word.lower(),aid))
                        terms_list.append(txt_desc)
                        txt_desc =""


            split_price = desc_split[1].split("<price>")
            price_split = split_price[1].split("</price>")
            price = price_split[0]


            desc = desc_split[0]

    #Do not add an entry with empty dates
            if date == "":
                pass
            else:
                txt_pdate +=("%s:%s,%s,%s\n"%(date,aid,cat,loc))
                date_list.append(txt_pdate)
                txt_pdate =""

    #Do not add an entry with empty prices
            if price == "":
                pass
            else:
                txt_price += ("%s:%s,%s,%s\n"%(price,aid,cat,loc))
                txt_price = txt_price.rjust(len(txt_price)+12 -(len(price)))
                price_list.append(txt_price)
                txt_price=""


            txt_ads+=("%s:%s"%(aid,line))
            ads_list.append(txt_ads)
            txt_ads= ""

#Adding: Files
    file_term = open("terms.txt","w")
    for i in terms_list:
        file_term.write(i)
    file_term.close()

    file_pdate = open("pdate.txt","w")
    for j in date_list:
        file_pdate.write(j)
    file_pdate.close()

    file_prices = open("prices.txt","w")
    for k in price_list:
        file_prices.write(k)
    file_prices.close()

    file_ads = open("ads.txt","w")
    for l in ads_list:
        file_ads.write(l)
    file_ads.close()

    print("Completed Phase 1\nCreated ads.txt, prices.txt, pdate.txt,terms.txt\n\n")

()
