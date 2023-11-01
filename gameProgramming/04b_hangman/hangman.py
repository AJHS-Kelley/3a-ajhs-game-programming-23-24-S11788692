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

def get

i = 0
while i < len (HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i+=1
