def order(sentence):

    sentencelist = sentence.split(' ')
    returnlist = {}

    for item in sentencelist:
        for char in item:
            try:
                char = int(char)
                returnlist[char] = item
            except:
                pass
    sentencestr = ''
    for item in returnlist:
        sentencestr = sentencestr + returnlist[item] + ' '

    return sentencestr.rstrip()
