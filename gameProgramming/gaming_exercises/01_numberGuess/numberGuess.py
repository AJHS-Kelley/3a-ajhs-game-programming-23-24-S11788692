#pick the sercret numberfrom the range of number
#you have a limit of 5 trys
  
#player guesses the number

#Frist to 3 points wins the game

#compare the sercret number
 
#If the guesses is correct what should happen?

       #award the player with a point|
 
       #print that they were correct|
 
#If the is incorrect what should happen?|

#Indicate if the guess is higher/lower|
 

#if the player isn't correct before the limit of trys, what happens|
 
#Award cpu a point|


 
#GUESSES a number tavion, myers v0.1
import random, tracemalloc, winsound
from PIL import image

tracemalloc.start()




#declarations

secretnumber = 21 # range 0--50 
playername = "" #empty string

#control numbers
playerscore= 0
cpuscore = 0
numguess = 0
playerguesses = 0
difficulty = None
numattempts = 6
rangemin = 0
rangemax = 0


losersound = None 
winnersound = None 

imagewin = None
imageloss = None 

print("""

          ||||||||||||||||||||||||||   
          |                        |
          |        Tavion          |
          |           M.           |
          |         Myers          |
          |                        |
          |+______________________+|


          """)

playerName = input("type your username\n press enter when your done.\n")
# verify input whenever you can.
print (f"you want me to call you {playerName}is that correct")

#PLAYERGUESS
print ("you need to guess a number 0 to 50. you have 5 guesses. Good Luck...")


while playerscore != 3 and cpuscore != 3: # Match Starts 

     secretnumber = random. randint(0, 50) # INLUSIVE
     print(f"player score {playerscore}.\n cpu score {cpuscore}\n")    
     numguess = 0         
     for guess in range(5): # Round Starts 
          playerGuess = int(input("Think of your number, type it in and then push enter "))
          print (f"You have picked {playerguesses}. Let's see if it is a match!\n")     
          if playerguesses == secretnumber: # Check to see if the player guessed correctly. 
               playerscore += 1 
               print("U got the secretnumber\n")
               break #immediately exit a loop
          else: 
               if playerguesses < secretnumber:
                    print(" your guess was lower than the secretnumber!\n")       
               else:
                    print("Your guess was higher than the secretnumber!\n")
          numguess += 1

     

     



playerGuess = input ("Think of your number, type it in and then push enter ")
print (f"You have picked {playerguesses}. Let's see if it is a match!\n")

if playerguesses != secretnumber:

cpuscore += 1
print ("The cpu won this round!\n")
imagelos.show()

if playerscore >=3:
     print ("you have won this rounds")
  imagewin.show()



print("Memory Usage: current,(peak)")
print (tracemalloc.get_traced_memory())
tracemalloc.stop() 

  



