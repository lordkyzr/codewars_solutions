#Brand new f strings in python 3.6!
def divisors_1(integer):
    return_arr = []
    for i in range(2,integer / 2):
        if integer % i == 0:
            return_arr.append(i)
    
    if len(return_arr) == 0:
        return f"{integer} is prime"
    else:
        return return_arr

#str.format way :(
def divisors_2(integer):
    return_arr = []
    for i in range(2,int(integer / 2) + 1):
        if integer % i == 0:
            return_arr.append(i)
    
    if len(return_arr) == 0:
        return "{} is prime".format(integer)
    else:
        return return_arr

#Python List Comprehension!
def divisors_3(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l        