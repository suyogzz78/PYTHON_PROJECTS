#creating a rock, paper, scissors game
#ask the user to make a choice between rock, paper, or scissors


import random 
while True:

    emojis={'r':'✊','p':'✋','s':'✌️'}#dictionary to store the emojis for each option
    options=('r','p','s')#using tuple to store the options

    user_input=input("Rock,Paper,Scissors? (r/p/s): ").lower()#taking input from the user and converting it to lower case
    if user_input not in options:
        print("please enter a valid value")
        

    computer_input=random.choice(options)#using random module to choose a random option for the computer
    print(f"you chose {emojis[user_input]} and the computer chose {emojis[computer_input]}")#displaying the choices of the user and the computer
    if user_input==computer_input:
        print("it's a tie")

    elif (
        (user_input== 'r'and computer_input=='s')or
        (user_input=='p' and computer_input=='r')or
        (user_input=='s' and computer_input=='p')):
        print("you win")

    else:
        print("you lose")   

    play_again=input("do you want to play again? (y/n): ").lower()#asking the user if he wants to play again

    if play_again =='n':
        print("thank you for playing")
        break