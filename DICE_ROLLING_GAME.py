#in this project we will create a simple dice rolling game
# where the user can  deicde whether to roll a dice or not  and the program will display the result
#we will create a loop such that the user will be able to roll the dice as many times as he wants
#we will use the random module to generate a random number between 1 and 6

import random #used to generate random numbers

while True:

  OPTION=  input("do you want to roll the dice (y/n ): ").lower() #convert the input to lower case

  if OPTION =='y':
            dice_roll1= random.randint(1,6)
            dice_roll2= random.randint(1,6)
            print("you rolled a ",dice_roll1," and ",dice_roll2)

  elif OPTION == 'n':
            print("thank you for playing")
            break
  
  else:
            print("invalid option, please enter y or n")
