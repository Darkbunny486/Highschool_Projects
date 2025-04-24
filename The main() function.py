import time
def division (x, y):
    if (y== 0):
        print ("Error, division by zero is not possible.")
    else:
        num = x/y
    return num

def multipy (x, y):
    num = x*y
    return num

def add (x, y):
    num = x + y
    return num

def sub (x, y):
    num = x - y
    return num
    
def printMenu ():
    print ("'WELCOME TO THE CALCULATOR PROGRAM\n")
    print ("Your options are:\n")
    print ("1. Addition")
    print ("2. Subtration")
    print ("3. Multiplication")
    print ("4. Divsion")
    print ("5. Quit Calcuation\n")
           
def get_option ():
    while (True):
        try:
            opt = int(input("Enter your option: "))
            if (opt <= 0) or (opt > 5):
                print ("Please pick one of the options")
            else:
                return opt
                break
        except:
            print ("Please pick one of the options using the numbers")

def get_num ():
    while (True):
        try:
            num = float(input("Enter a number: "))
            return num
            break
        except:
            print("Please enter a valid number")

def do_calculations (opt):
    num1 = get_num ()
    num2 = get_num ()
    if (opt == 1):
        answer = add (num1, num2)
    elif (opt == 2):
        answer = sub (num1, num2)
    elif (opt == 3):
        answer = multipy (num1, num2)
    else:
        answer = division (num1, num2)
    print ("The answer is", round(answer, 2))

def main ():
    printMenu ()
    opt = get_option ()
    while (opt != 5):
        do_calculations (opt)
        time.sleep (0.5)
        printMenu ()
        opt = get_option ()

    print ("Thank you for using the calculator")

main ()







