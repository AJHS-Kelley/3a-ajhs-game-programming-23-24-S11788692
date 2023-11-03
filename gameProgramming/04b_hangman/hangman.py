import random
wordlist = 'butter vest coast venmon spiderman joker turtle jacksonville dogfood pasta baseball dog money monkey batman'.split()
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
   ======''',  '''
+----+
O    |
     |
     |
     |
     |
   ======''',  '''
+----+
O    |    
|    |
     |
     |
   ======''',  '''
+----+
O    |    
|\   |
     |
     |
   ======''',  '''
+----+
 O   |    
/|\  |
     |
     |
   ======''',  '''
+----+
 O   |    
/|\  |
/    |
     |
   ======''',  '''
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

def displayboard (missedletters, correctletters, secretword):
    print(HANGMAN_BOARD[len (missedletters)])
    print()

i = 0
while i < len(HANGMAN_BOARD):
  print(HANGMAN_BOARD[i])
  i += 1

print('missed letters:', end = ' ' )
for letter in missedletters:
        print(?, end = ' ')
    print()

    blanks = '_' * len(secretword)

    for i in range(len(secretword)):
      if secretword[i] in correctletters:
        blanks = blanks[:i] + secretword[i] + blanks[i+1:]
        #the : character is used to slice strings into pieces.
        blanks[:0] +