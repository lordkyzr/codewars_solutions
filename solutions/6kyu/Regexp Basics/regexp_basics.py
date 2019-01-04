import re

def ipv4_address(address):

    for char in address:
        if char.isdigit() == False:
            if char != ".":
                return False

    results = re.search('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$',address)
    if results == None:
        return False
    else:
        return True