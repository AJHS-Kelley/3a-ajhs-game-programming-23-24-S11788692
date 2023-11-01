import random
wordlist = 'Butter,vest,coast,venmon,spiderman,joker,turtle,jacksonville,dogfood,pasta,baseball,dog,money,monkey,batman'.split()
print(wordlist)
print (wordlist[0])
# VARIABLE_NAMES that are CAPS are contants and not meant to change. 
HANGMAN_BOARD =['''
+----+
     |
     |
     |
     |
     |
   ======'''  '''
+----+
O    |
     |
     |
     |
     |
   ======'''  '''
+----+
O    |    
|    |
     |
     |
   ======'''  '''
+----+
O    |    
|\   |
     |
     |
   ======'''  '''
+----+
 O   |    
/|\  |
     |
     |
   ======'''  '''
+----+
 O   |    
/|\  |
/    |
     |
   ======'''  '''
+----+
 O   |    
/|\  |
/ \  |
     |
   ======''']

def getRandomWord(wordlist):
    wordIndex = random.randint(0 , len(wordlist) - 1)
    # len(listname) -1 
    
    print(wordIndex)
    return wordlist[wordIndex]

def displayboard (incorrectletters, correctletters, sercertword):
    print(HANGMAN_BOARD[len (incorrectletters)])
    print()

i = 0
while i < 99:
    getRandomWord(wordlist)
    i += 1
