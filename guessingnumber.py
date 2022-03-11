import random

User_name = input("Enter your name ")

this_number = random.randint(0,100)

guess = -1

while(guess != this_number):
    guess = int(input("guess the number"))
    if(guess < this_number):
        print("Sorry {}, Your guess {} is too low".format(User_name,guess))
    elif(guess > this_number):
        print("Sorry {}, Your guess {} is too high". format(User_name,guess))
    else:
        print("Excellent {}, you guess {} is correct, you win the game". format(User_name,guess))
