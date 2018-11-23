import re
from bsddb3 import db

# global variable to determine if user wants to display the short form or not
SHORT_INPUT = True # set to true by default

def dateQuery(queryString):
    #query string is of the format date<=yyyy/mm/dd or with an equivalent operator
    #We need to split this string in order to conduct the query TODO

    return 0


def priceQuery(queryString, categoryQueries, locationQueries):
    # queryString is of the format price<=[/number]+
    # TODO: format the string so you can conduct queries on it
    queryString = queryString.lower()

    # Extract the number from the price string
    price = re.split('<=|>=|>|<', queryString)[1]
    # http://www.datasciencemadesimple.com/add-spaces-in-python/ adding spaces to string
    # we need to pad the price with leading spaces because thats how theyre stored in the DB
    num_of_spaces = 12
    price = price.rjust(num_of_spaces)
    #print(len(price))
    # extract the boolean operator from the query string
    operator = re.findall('(?:<=|>=|>|<)', queryString)[0]
    price = bytes(price, encoding='utf-8')

    # initialize price index DB and ad index DB
    priceIndex = db.DB()
    priceIndex.open("pr.idx")
    priceCursor = priceIndex.cursor()
    adIndex = db.DB()
    adIndex.open("ad.idx")
    adCursor = adIndex.cursor()

    priceCursor.set_range(price) # will set to the smallest key greater than or equal to the specified key

    try:
        priceCursor.get(price, db.DB_CURRENT)
    except:
        print("No Record with Specified Price Range Found")  # checks to see if term was found
        exit()

    adIds = []

    if operator == '>=':

        while priceCursor.get(price, db.DB_CURRENT)[0] >= price:

            # get the values of the keys and append to list of values
            retrievedValue = priceCursor.get(price, db.DB_CURRENT)[1]
            retrievedValue = retrievedValue.decode('utf-8')  # adId is in first position

            # determine if we need to meet location or category conditions
            if categoryQueries or locationQueries:
                if categoryQueries:
                    category = categoryQueries[0]
                    # get the category (there should only be one category)
                    category = category.replace(" ", "")  # get rid of white space so we can split it
                    catTerm = category.split("=")[1]

                    # Now check if the retrieved value has a corresponding category value as catTerm
                    if catTerm != retrievedValue.split(",")[1].lower():
                        if priceCursor.get(price, db.DB_NEXT) == None:
                            break  # no match so we need to continue
                        continue

                if locationQueries:
                    location = locationQueries[0]
                    # get the category
                    location = location.replace(" ", "")  # get rid of white space so we can split it
                    locTerm = location.split("=")[1]
                    # Now check if the retrieved value has a corresponding category value as catTerm

                    if locTerm != retrievedValue.split(",")[2].lower():
                        if priceCursor.get(price, db.DB_NEXT) == None:
                            break  # no match so we need to continue
                        continue
                # if we reach this point we can append the adID
                adIds.append(retrievedValue.split(',')[0])

            else:  # if there are no categories or locations to check then add the adID to the list
                adIds.append(retrievedValue.split(',')[0])

            if priceCursor.get(price, db.DB_NEXT) == None:
                break

    elif operator == '>':

        if priceCursor.get(price, db.DB_CURRENT)[0] == price:
            # if the set index is exactly the price specified then move to next one if possible
            if priceCursor.get(price, db.DB_NEXT) == None:
                return []

        while priceCursor.get(price, db.DB_CURRENT)[0] > price:

            # get the values of the keys and append to list of values
            retrievedValue = priceCursor.get(price, db.DB_CURRENT)[1]
            retrievedValue = retrievedValue.decode('utf-8')  # adId is in first position

            # determine if we need to meet location or category conditions
            if categoryQueries or locationQueries:
                if categoryQueries:
                    category = categoryQueries[0]
                    # get the category (there should only be one category)
                    category = category.replace(" ", "")  # get rid of white space so we can split it
                    catTerm = category.split("=")[1]

                    # Now check if the retrieved value has a corresponding category value as catTerm
                    if catTerm != retrievedValue.split(",")[1].lower():
                        if priceCursor.get(price, db.DB_NEXT) == None:
                            break  # no match so we need to continue
                        continue

                if locationQueries:
                    location = locationQueries[0]
                    # get the category
                    location = location.replace(" ", "")  # get rid of white space so we can split it
                    locTerm = location.split("=")[1]
                    # Now check if the retrieved value has a corresponding category value as catTerm

                    if locTerm != retrievedValue.split(",")[2].lower():
                        if priceCursor.get(price, db.DB_NEXT) == None:
                            break  # no match so we need to continue
                        continue
                # if we reach this point we can append the adID
                adIds.append(retrievedValue.split(',')[0])

            else:  # if there are no categories or locations to check then add the adID to the list
                adIds.append(retrievedValue.split(',')[0])

            if priceCursor.get(price, db.DB_NEXT) == None:
                break

    elif operator == '<=':
        if priceCursor.get(price, db.DB_CURRENT)[0] != price:  # need to got to previous index due to how the set_range function works
            priceCursor.prev()                                  # set to previous if set key is initially larger than price

        while priceCursor.get(price, db.DB_CURRENT)[0] <= price:

            # get the values of the keys and append to list of values
            retrievedValue = priceCursor.get(price, db.DB_CURRENT)[1]
            retrievedValue = retrievedValue.decode('utf-8')  # adId is in first position

            # determine if we need to meet location or category conditions
            if categoryQueries or locationQueries:
                if categoryQueries:
                    category = categoryQueries[0]
                    # get the category (there should only be one category)
                    category = category.replace(" ", "")  # get rid of white space so we can split it
                    catTerm = category.split("=")[1]

                    # Now check if the retrieved value has a corresponding category value as catTerm
                    if catTerm != retrievedValue.split(",")[1].lower():
                        if priceCursor.get(price, db.DB_PREV) == None:
                            break  # no match so we need to continue
                        continue

                if locationQueries:
                    location = locationQueries[0]
                    # get the category
                    location = location.replace(" ", "")  # get rid of white space so we can split it
                    locTerm = location.split("=")[1]
                    # Now check if the retrieved value has a corresponding category value as catTerm

                    if locTerm != retrievedValue.split(",")[2].lower():
                        if priceCursor.get(price, db.DB_PREV) == None:
                            break  # no match so we need to continue
                        continue
                # if we reach this point we can append the adID
                adIds.append(retrievedValue.split(',')[0])

            else:  # if there are no categories or locations then add the adID to the list
                adIds.append(retrievedValue.split(',')[0])

            if priceCursor.get(price, db.DB_PREV) == None:
                break


    elif operator == '<':
        priceCursor.get(price, db.DB_PREV)  # need to got to previous index due to how the set_range function works

        while priceCursor.get(price, db.DB_CURRENT)[0] < price:

            # get the values of the keys and append to list of values
            retrievedValue = priceCursor.get(price, db.DB_CURRENT)[1]
            retrievedValue = retrievedValue.decode('utf-8')  # adId is in first position

            # determine if we need to meet location or category conditions
            if categoryQueries or locationQueries:
                if categoryQueries:
                    category = categoryQueries[0]
                    # get the category (there should only be one category)
                    category = category.replace(" ", "")  # get rid of white space so we can split it
                    catTerm = category.split("=")[1]

                    # Now check if the retrieved value has a corresponding category value as catTerm
                    if catTerm != retrievedValue.split(",")[1].lower():
                        if priceCursor.get(price, db.DB_PREV) == None:
                            break  # no match so we need to continue
                        continue

                if locationQueries:
                    location = locationQueries[0]
                    # get the category
                    location = location.replace(" ", "")  # get rid of white space so we can split it
                    locTerm = location.split("=")[1]
                    # Now check if the retrieved value has a corresponding category value as catTerm

                    if locTerm != retrievedValue.split(",")[2].lower():
                        if priceCursor.get(price, db.DB_PREV) == None:
                            break  # no match so we need to continue
                        continue

                # if we reach this point we can append the adID
                adIds.append(retrievedValue.split(',')[0])

            else:  # if there are no categories or locations then add the adID to the list
                adIds.append(retrievedValue.split(',')[0])

            if priceCursor.get(price, db.DB_PREV) == None: # have to go backwards until beginning is reached
                break

    # Now that we have the adIds we can get their titles from ad.idx
    fullRecords = []
    adIds = list(set(adIds)) # get rid of duplicates
    for adId in adIds:
        # we are guaranteed to find the ads in ad.idx
        adId = bytes(adId, encoding='utf-8')
        adCursor.set(adId)
        record = adCursor.get(adId, db.DB_CURRENT)

        # now that we have the record we can return the ID as well as the ad record
        fullRecords.append((adId.decode('utf-8'), record[1].decode('utf-8')))

    return fullRecords

def locationQuery(queryString):
    # queryString is of the format location=[A-Za-z0-9]+
    # TODO: format the string so you can conduct queries on it
    return []

def categoryQuery(queryString):
    # queryString is of the format category=[A-Za-z0-9]+
    # TODO: format the string so you can conduct queries on it
    return []

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
    adCursor = adIndex.cursor()

    # We first need to get the ad id from the term

    termCursor.set(queryString)

    try:
        termCursor.get(queryString, db.DB_CURRENT)
    except:
        print("No term found") # checks to see if term was found
        exit()

    # At this point the cursor is set correctly and we need to iterate through
    # all values that match the desired key
    adIds = []
    fullRecords = []
    while termCursor.get(queryString, db.DB_CURRENT)[0] == queryString:
        # get the values of the keys and append to list of values
        retrievedValue = termCursor.get(queryString, db.DB_CURRENT)[1]
        retrievedValue = retrievedValue.decode('utf-8')
        adIds.append(retrievedValue)
        termCursor.next()

    #Now that we have the adIds we can get their titles from ad.idx
    for adId in adIds:
        # we are guaranteed to find the ads in ad.idx
        adId = bytes(adId, encoding='utf-8')
        adCursor.set(adId)
        record = adCursor.get(adId, db.DB_CURRENT)

        # now that we have the record we can return the ID as well as the ad record
        fullRecords.append((adId.decode('utf-8'), record[1].decode('utf-8')))

    return fullRecords

def printRecord(record):
    if SHORT_INPUT == True:
        # First we need to extract the title from the the record
        # I will use regular expressions for this
        title = re.findall(r'<ti>.*</ti>', record[1])[0]
        title = title.replace('<ti>', "")
        title = title.replace('</ti>', "")

        print('adID: {}'.format(record[0]))
        print('Title: {}\n'.format(title))
        return

    else:
        print("adID: {}".format(record[0]))
        print("Record: {}\n".format(record[1]))
        return

def main():
    # 'Master' list that will contain all the returned results from all queries
    global SHORT_INPUT
    resultList = []

    userInput = input("Type in Query: ")
    userInput = userInput.lower()

    if userInput == "exit":
        exit(1)

    elif userInput == "output=brief":
        print("Short Display Enabled")
        SHORT_INPUT = True
        return

    elif userInput == "output=full":
        print("Full Display Enabled")
        SHORT_INPUT = False
        return

    # Search for all category Queries
    categoryList = re.findall(r'cat\s*=\s*[0-9A-Za-z%\-]+', userInput)
    if len(categoryList) > 1:
        # cannot have more than one category
        print("No Matches")
        return

    for category in categoryList:
        # first remove the price string from the userInput
        userInput = userInput.replace(category, "")
        category = category.replace(" ", "")
        # We do not execute the category query yet since we want to see
        # if we can execute it simultaneously with price or date
        #
        # result = categoryQuery(category)
        # resultList = resulitList + result



    # Search for all location Queries
    locationList = re.findall(r'location\s*=\s*[0-9A-Za-z\-]+', userInput)

    if len(locationList) > 1:
        # cannot have more than one location
        print("No Matches")
        return

    for location in locationList:
        # first remove the price string from the userInput
        userInput = userInput.replace(location, "")
        location = location.replace(" ", "")
        # We do not execute the location query yet since we want to see
        # if we can execute it simultaneously with price or date
        #
        # result = locationQuery(category)
        # resultList = resultList + result

    # Search for all dateQueries
    dateList = re.findall(r'.*date\s*(?:<=|>=|>|<)\s*[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]', userInput)
    for date in dateList:
        # first remove the date string from the userinput
        userInput = userInput.replace(date, "")
        date = date.replace(" ","")
        result = dateQuery(date)
        resultList = resultList + result


    # Search for all Price Queries
    priceList = re.findall(r'price\s*(?:<=|>=|>|<)\s*[0-9]+', userInput)
    for price in priceList:
        # first remove the price string from the userInput
        userInput = userInput.replace(price, "")
        price = price.replace(" ", "")
        result = priceQuery(price, categoryList, locationList)
        # If there are already results in the result list, then take the intersection. Otherwise the just the result
        # to the result list
        if not resultList:
            resultList = resultList + result

        else:
            resultList = list(set(resultList) - (set(resultList) - set(result)))


    # Once we get to this points, all thats left are the terms that the user wants to search for
    # since all the other query strings will have been removed from the userInput string
    termList = re.findall(r'\w+\s*', userInput)
    termList = list(filter(None, termList))
    for term in termList:
        term = term.replace(" ", "")
        result = termQuery(term)
        # If there are already results in the result list, then take the intersection. Otherwise the just the result
        # to the result list
        if not resultList:
            resultList = resultList + result

        else:
            resultList = list(set(resultList) - (set(resultList) - set(result)))

    # if the category query was not handled by price or date query then we execute the worst possible scenario
    if not dateList and not priceList:
        if categoryList:
            result = categoryQuery(categoryList[0])
            resultList = resultList + result;

        if locationList:
            result = locationQuery(locationList[0])
            if not resultList:
                resultList = resultList + result;

            else: # if the category query returned results we need to take the intersection
                resultList = list(set(resultList)- (set(resultList) - set(result)))

    if not resultList:
        print("No matches found")


    # at this point all the results should be loaded in the result list and we can display them
    for record in resultList:
        printRecord(record)

    return





while(1):
    main()