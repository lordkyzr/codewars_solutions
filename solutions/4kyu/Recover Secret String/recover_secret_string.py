def recoverSecret(triplets):
    r = []
    #Create list of characters
    for charset in triplets:
        for i in charset:
            r.append(i)
    #Convert that to a unique set of characters and then turn it to a unique list since set gives you an iterable of hashes
    r = list(set(r))

    #Go over each char and start reordering our unique chars based on their position in the passed in list
    for lst in triplets:
        #Start at the back of the list
        shuffle(r, lst[1], lst[2])
        #Now do the front of the list
        shuffle(r, lst[0], lst[1])
    return ''.join(r)

#shuffle moves our unqiue items around based 
def shuffle(lst, a, b):
    #If the first character exists after the second in position shuffle it in our unique list
    if lst.index(a) > lst.index(b):
        lst.remove(a)
        lst.insert(lst.index(b), a)

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets), secret)