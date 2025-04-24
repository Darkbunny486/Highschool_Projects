from random import *

num = randint(1, 100)
ask = "Yes"
while (ask != "No") and (ask != "no"):   
    for a in range (1, num):
        rem = num % a
        if (rem == 0):
            print ("Factors:", a, int(num/a))
    ask = str(input("Would you like to play again?\n"))
        
    

