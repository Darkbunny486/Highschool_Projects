from random import *
import time
num = randint(1, 100)

def hard ():
    guessNum = 0
    n = 0
    for a in range (5):
        while (True):
            try:
                user = int(input("Guess the number: "))
                guessNum = guessNum + 1
                break
            except:
                print ("That was not a number")
                a = a - 1
        if (user > num):
            print ("Too high")
        elif (user< num):
            print ("Too low")
        else:
            print ("You win!")
            print ("The number of guesses it took was", guessNum)
            n = 1
            break
    if (n == 0):
        print ("You lost, the number you were trying to guess was", num)

def easy():
    guessNum = 0
    n = 0
    for a in range (15):
        while (True):
            try:
                user = int(input("Guess the number: "))
                guessNum = guessNum + 1
                break
            except:
                print ("That was not a number")
                a = a - 1
        if (user > num):
            print ("Too high")
        elif (user< num):
            print ("Too low")
        else:
            print ("You win!")
            print ("The number of guesses it took was", guessNum)
            n = 1
            break
    if (n == 0):
        print ("You lost, the number you were trying to guess was", num)

def medium():
    guessNum = 0
    n = 0
    for a in range (10):
        while (True):
            try:
                user = int(input("Guess the number: "))
                guessNum = guessNum + 1
                break
            except:
                print ("That was not a number")
                a = a - 1
        if (user > num):
            print ("Too high")
        elif (user< num):
            print ("Too low")
        else:
            print ("You win!")
            print ("The number of guesses it took was", guessNum)
            n = 1
            break
    if (n == 0):
        print ("You lost, the number you were trying to guess was", num)


while (True):
    time.sleep (0.5)
    print ("Welcome to the guessing game!")
    print (''' Would you like to play?
        1. Hard
        2. Medium
        3. Easy
        4. Exit
        ''')
    try:
        again = int(input("Please use the number to choose one of the options\n"))
        if (again == 1):
            hard ()
        elif (again == 2):
            medium ()
        elif (again == 3):
            easy ()
        elif (again == 4):
            break
        else:
            print ("That was not an option")
    except:
        print("That was not a number, or any of the options")






    

