#Guess the number game

import random

guesses = 6
number = random.randint(1,100)
string_number = str(number) 
win = False
while guesses > 0:
    guess = int(input("Guess a number 1-100 good luck: "))

    guesses -= 1
    string_guesses = str(guesses) 

    if guess > number:
        print("Your guess was too high, you have " + string_guesses + " remaining.")
    elif guess < number:
        print("your guess was too low , you have " + string_guesses + " remaining.")
    else:
        print ("You won!!!!!!!!")
        win = True
        guesses = 0


if win == False:
    print("Sorry you're a loser, the number was " + string_number + ".") 
