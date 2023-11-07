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
        
       for letter in blanks:
        print(letter, end = ' ')
    print()

    def getguess(alreadyguessed):
      #Only aqllow: single caracter, A-Z only, not guessed already.
      while True: # default 'infinite' loop
        print('please guess a letter to guess the secretword.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
          print('please enter one character.\n')
          elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('please enter an engkish letter only.')
            elif guess in alrealdyguess:
              print('Already guessed. please guess a different letter!')
              else:
                  return guess 

def playagain():
  print('Would u like to play again? text Yes or No.')
  return input().lower().starswith(' y ') # rturn True/False based on the input.
  print('Let\'s play Hangman!)
  missedletters = ''
  correctletters = ''
  secretword = getRandomWord(wordlist)
  print('testing sercret word:' + secretword)
  gameisdone = False
# Game loop begin here
while True: # Two ways to exit while True: return OR break
    displayboard(missedletters, correctletters, secretword)

    guess = getguess(missedletters + correctletters)
    
    if guess in secretword: # Is the guess in the sercretword?
      correctletters = correctletters + guess 

      # check for vivtory 
      foundAllLetters = True 
      for i in range (len(secretword)):
        if secretword[i] not in correctletters:
          foundAllLetters = False
          break
      if foundAllLetters:
        print('Congraulations!')
        gameisdone = True   