

ar = ["o", "as", "a", "amos", "ais", "an"]
er = [ "o", "es", "e", "emos", "eis", "en"]
ir = ["o", "es", "e", "imos", "is", "en"]
endings ={ "ar" :ar, "er":er, "ir":ir}

words = [["to buy", "comprar"],["to speak", "hablar"],["to learn", "apprender"], ["to recieve", "recibir"]]

def getverb(v):
    for i in range(0, len(words)):
        if v == words[i][0]:
            return words[i][1]

def getEnding(v):
    frstltr = len(v) - 2
    sndltr = len(v) - 1
    return str(v[frstltr]) + str(v[sndltr])


def verb_noend(v):
    verb = str(v)
    verbnoend = ""
    for i in range(0, (len(verb)-2)):
        verbnoend += verb[i]
    return verbnoend

def conjugate(v):
    verb = getverb(v)
    if verb == None:
        return []
    verb_noending = str(verb_noend(verb))
    ending = getEnding(verb)
    conjugatedlst = []
    for i in range(0, len(endings[ending])):
        conjugatedlst.append(verb_noending + str(endings[ending][i]))
   
    return conjugatedlst


print(getverb("to buy"))
print(getverb("to see"))
print(getEnding("comprar"))
print(getEnding("apprender"))
print(conjugate("to buy"))
print(conjugate("to learn"))
print(conjugate("to see"))
print(conjugate("to recieve"))