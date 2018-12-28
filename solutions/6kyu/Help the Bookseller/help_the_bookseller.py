import re
def stock_list(listOfArt, listOfCat):
    return_obj = {}
    for category in listOfCat:
        sum = 0
        for art in listOfArt:
            if art[0] == category:
                result = re.search(r"(\d*)$",art)
                if result:
                    result = int(result.group(0))
                    sum += result
        return_obj[category] = sum
    return_str = ""
    buildStr = False
    for item in return_obj:
        if return_obj[item] > 0:
            buildStr = True
    if buildStr == True:
        for category in listOfCat:
            return_str += "(" + str(category) + " : " + str(return_obj[category]) + ") - "
        return return_str[:-3]
    else:
        return ''