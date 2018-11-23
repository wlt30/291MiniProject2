import re
from bsddb3 import db

def dateQuery(queryString):
    #query string is of the format date<=yyyy/mm/dd or with an equivalent operator
    #We need to split this string in order to conduct the query TODO

    return 0

def priceQuery(queryString):
    #queryString is of the format price<=[/number]+
    #TODO: format the string so you can conduct queries on it
    return 0

def locationQuery(queryString):
    # queryString is of the format location=[A-Za-z0-9]+
    # TODO: format the string so you can conduct queries on it
    return 0

def categoryQuery(queryString):
    # queryString is of the format category=[A-Za-z0-9]+
    # TODO: format the string so you can conduct queries on it
    return

def termQuery(queryString):
    # queryString is the term the user wants to search
    # TODO: format the string so you can conduct queries on it
    queryString = queryString.lower()
    # Setting byte literals https://stackoverflow.com/questions/19511440/add-b-prefix-to-python-variable
    queryString = bytes(queryString, encoding='utf-8')
    # we need the term index and the ad index
    termIndex = db.DB()
    termIndex.open("te.idx")
    termCursor = termIndex.cursor()
    adIndex = db.DB()
    adIndex.open("ad.idx")
    adIndex.cursor()

    # We first need to get the ad id from the term

    termCursor.set(queryString)

    try:
        print(termCursor.get(queryString, db.DB_CURRENT))
    except:
        print("No term found") # checks to see if term was found
        return

    # At this point the cursor is set correctly and we need to iterate through
    # all values that match the desired key
    adIds = []
    while termCursor.get(queryString, db.DB_CURRENT)[0] == queryString:
        # get the values of the keys and append to list of values
        retrievedValue = termCursor.get(queryString, db.DB_CURRENT)[1]
        retrievedValue = retrievedValue.decode('utf-8')
        adIds.append(retrievedValue)
        termCursor.next()

    #Now that we have the adIds we can get their titles from ad.idx
    for adId in adIds:
        # we are guaranteed to find the ads in ad.idx



    return

def main():
    # 'Master' list that will contain all the returned results from all queries
    resultList = []

    userInput = input("Type in Query: ")
    print(userInput)

    # Search for all dateQueries
    dateList = re.findall(r'.*date\s*(?:<=|>=|>|<)\s*[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]', userInput)
    for date in dateList:
        #first remove the date string from the userinput
        userInput = userInput.replace(date, "")
        date = date.replace(" ","")
        result = dateQuery(date)
        resultList.append(result)


    # Search for all Price Queries
    priceList = re.findall(r'price\s*(?:<=|>=|>|<)\s*[0-9]+', userInput)
    for price in priceList:
        # first remove the price string from the userInput
        userInput = userInput.replace(price, "")
        price = price.replace(" ", "")
        result = priceQuery(price)
        resultList.append(result)


    # Search for all location Queries
    locationList = re.findall(r'location\s*=\s*[0-9A-Za-z]+', userInput)
    for location in locationList:
        # first remove the price string from the userInput
        userInput = userInput.replace(location, "")
        location = location.replace(" ", "")
        result = locationQuery(location)
        resultList.append(result)



    # Search for all category Queries
    categoryList = re.findall(r'cat\s*=\s*[0-9A-Za-z%\-]+', userInput)
    for category in categoryList:
        # first remove the price string from the userInput
        userInput = userInput.replace(category, "")
        category = category.replace(" ", "")
        result = categoryQuery(category)
        resultList.append(result)



    # Once we get to this points, all thats left are the terms that the user wants to search for
    # since all the other query strings will have been removed from the userInput string
    termList = re.findall(r'\s*.*\s*', userInput)
    termList = list(filter(None, termList))
    for term in termList:
        term = term.replace(" ", "")
        result = termQuery(term)
        resultList.append(result)


    termIndex = db.DB()
    termIndex.open("te.idx")
    termCursor = termIndex.cursor()

    return






main()