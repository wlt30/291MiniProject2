import os
import xml.etree.ElementTree as et


def phase1(small_file, big_file):
    tree = et.parse("10.txt")
    root = tree.getroot()

    # for child in root:
    #     print(child.tag)
    term_txt =[]
    pdate_txt =[]
    price_txt =[]
    ads_txt=[]
    term =""
    aid = ""
    date = ""
    category = ""
    location = ""
    price =""
    main_tag=""
    description=""

    txt_term =""
    txt_price =""
    txt_pdate =""
    txt_ads =""

    description=""


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
                    txt_price = ("%s:%s:%s:%s\n"%(price,aid,category,location))
                    price_txt.append(txt_price)
                    txt_price=""
        print(category);
        txt_ads = ("%s:<ad><aid>%s</aid><date>%s</date><loc>%s</loc><cat>%s</cat><ti>%s</ti><desc>%s</desc><price>%s</price></ad>\n"%(aid,aid,date,location,category,term,description,price))
        if txt_ads not in ads_txt:
            ads_txt.append(txt_ads)  #Gets rid of extra line if i don't check
        txt_ads = ""


    file_term = open("terms.txt","w")
    for i in term_txt:
        file_term.write(i)
    file_term.close()

    file_pdate = open("pdate.txt","w")
    for j in pdate_txt:
        file_pdate.write(j)
    file_pdate.close()

    file_prices = open("prices.txt","w")
    for k in price_txt:
        file_prices.write(k)
    file_prices.close()

    file_ads = open("ads.txt","w")
    for l in ads_txt:
        file_ads.write(l)
    file_ads.close()










    # for i in term_txt:
    #     print(i)
    # for j in pdate_txt:
    #     print(j)
    # for k in price_txt:
    #     print(k)
    # for l in ads_txt:
    #     print(l)

#TO DO ADD CONDITION TO TERMS!



def main():
    #test("test.txt","test.txt")
    phase1("10test.txt","1k.txt")







main()


# def test(f1,f2):  #10-terms, 1kterms
#     f = open(f1 , "r")
#
#     f1 = f.readlines()
#     print(f1)
#
#     term = ""
#     list = []
#     for line in f1:
#         for letter in line:
#             if letter == "&": #ignore all special characters
#                 break
#             if letter == ':':
#                 if len(term) <=2:
#                     break
#                 else:
#
#                     term += '\n'
#                     list.append(term.lower())
#                     term =""
#                     break
#             else:
#                 term += letter
#
#
#     print("-----writing-----")
#     x = open("result.txt", "w+")
#     for i in list:
#         x.write(i)
#     x.close()   #savese the files
#
#     print("----- Reading Files-----")
#     z = open("result.txt","r")
#
#     z1 = z.readlines()
#     print(z1)
