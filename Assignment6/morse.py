code = {"A":"=.===",
        "B":"===.=.=.=",
        "C":"===.=.===.=",
        "D":"===.=.=",
        "E":"=",
        "F":"=.=.===.=",
        "G":"===.===.=",
        "H":"=.=.=.=",
        "I":"=.=",
        "J":"=.===.===.===",
        "K":"===.=.===",
        "L":"=.===.=.=",
        "M":"===.===",
        "N":"===.=",
        "O":"===.===.===",
        "P":"=.===.===.=",
        "Q":"===.===.=.===",
        "R":"=.===.=",
        "S":"=.=.=",
        "T":"===",
        "U":"=.=.===",
        "V":"=.=.=.===",
        "W":"=.===.===",
        "X":"===.=.=.===",
        "Y":"===.=.===.===",
        "Z":"===.===.=.="}

d = {}
for k,v in code.items():
    d[v] = k

def letter_to_code(letter):
    return code[letter]

space_between_letters= "..."
space_between_words= "......."

def word_to_code(word):
   word = word.upper()
   codeofword=""
   for i in range(len(word)):
       if i == (len(word)-1):
           x = letter_to_code(word[i])
           codeofword += x
           return codeofword
       else:
           x = letter_to_code(word[i]) + space_between_letters
           codeofword += x

def sentence_to_code(s):
    wordsins = s.split()
    translation = ""
    for i in range(len(wordsins)):
        if i == (len(wordsins)-1):
            x = word_to_code(wordsins[i])
            translation += x
            return translation
        else:
            x = word_to_code(wordsins[i]) + space_between_words
            translation += x

def code_to_letters(s):
    return d[s]

def code_to_word(s):
    lstfolttrs =s.split(space_between_letters)
    word = ""
    for i in lstfolttrs:
        x = code_to_letters(i)
        word += x
    return word

def code_to_sentence(s):
    lstowrds = s.split(space_between_words)
    sentence = ""
    for i in range(len(lstowrds)):
        if i == (len(lstowrds)-1):
            x = code_to_word(lstowrds[i])
            sentence += x
            return sentence
        else:
            x = code_to_word(lstowrds[i]) + " "
            sentence += x


def testing(s,c):
    if sentence_to_code(s) == c:
        print("S->C for {0} passed.".format(s))
    else:
        print("S->c for {0} failed.".format(s))
    if code_to_sentence(c) == s:
        print("C->S for {0} passed.".format(s))
    else:
        print("C->S for {0} failed.".format(s))
    
test_strings = ["MORSE CODE", "I NEED MONEY", "ORDER PIZZA"]
test_code = ["===.===...===.===.===...=.===.=...=.=.=...=.......===.=.===.=...===.===.===...===.=.=...=",
             "=.=.......===.=...=...=...===.=.=.......===.===...===.===.===...===.=...=...===.=.===.===",
             "===.===.===...=.===.=...===.=.=...=...=.===.=.......=.===.===.=...=.=...===.===.=.=...===.===.=.=...=.==="]

#for s,c in zip(test_strings, test_code):
   # testing(s,c)

#with open("c.txt") as c:
 #   Mcode = c.read().splitlines()
#for line in Mcode:
 #   print(code_to_sentence(line))

print(sentence_to_code("I dont know"))


