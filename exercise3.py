from random import randint
number = randint(0,100)
guess = None
while guess != number:
    guess = int(input("Pick a number randomly: "))
    if guess == number:
        print("You won! :)")
        break
    if guess < number:
       print("Increase your number! :(")
    else:
        print("Decrease your number! :(")

