def prime (user):
    num = 0
    for a in range (1, user):
        rem = user % a
        if (rem == 0):
            num = num + 2
        if (num == 2):
            pri = True
        else:
            pri = False
    return pri

def tryAgain ():
    again = "yes"
    while (again == "yes") or (again == "Yes"):
        user = int(input("Enter a number: "))
        print(prime (user))
        try:
            again = input("Would you like to play again?\n")
        except:
            print ("That was not a yes or no, it wasn't even letters")
            again = input("Would you like to play again?\n")
        
tryAgain ()


