def get_num ():
    """Returns a float number
    
    Returns:
            num(float): A float taken from the user
    """
    while (True):
        try:
            num = float(input("Enter a number: "))
            break
        except:
            print ("Please enter a number")
    return num

def get_int():
    """Returns an interger
    
    Returns:
            num(int): An integer taken from the user
    """
    while (True):
        try:
            num = int(input("Enter a integer: "))
            break
        except:
            print ("Please enter a number")
    return num

def get_postive (flag):
    """Returns a positive integer greater than 0 or equal to zero depending on flag
    
    Args:
            flag(boolean): Determines if zero is allowed or not
            
    Returns:
            num(int): An interger taken from the user
    """
    if (flag == False):
        while (True):
            try:
                num = int(input("Enter a number greater than zero: "))
                if (num > 0):
                    break
                else:
                    print ("Not an option")
            except:
                print ("Not an option")
    else:
        while (True):
            try:
                num = int(input("Enter a number greater than or equal to zero: "))
                if (num >= 0):
                    break
                else:
                    print ("Not an option")
            except:
                print("Not an option")
    return num

def get_option (n):
    """Returns an integer between 1 and n
    
    Args:
            n(int): Determines the range of the options
            Assumptions: n > 0
    
    Returns:
            option(int): An integer taken from the user
    """
    while (True):
        try:
            option = int(input("Enter your option: "))
            if option in range (1, n+1):
                break
            else:
                print ("Pick one of the options")
        except:
            print ("Pick one of the options")

def main ():
    get_option (5)
    
if __name__ == '__main__':
    main ()

        