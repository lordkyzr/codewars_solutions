#Method 1 List Comprehension
def getCount_1(inputStr):
    num_vowels = 0
    num_vowels = sum([num_vowels + 1 for i in inputStr if i in ["a","e","i","o","u"]])
    return num_vowels

#Method 2 more verbose/readable way
def getCount_2(inputStr):
    num_vowels = 0
    for i in inputStr:
        if i in ["a","e","i","o","u"]:
            num_vowels += 1
    return num_vowels

#Method 3 The Elusive Python One Liner
def getCount_3(inputStr):
    return sum(i in 'aeiou' for i in inputStr)