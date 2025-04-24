#Arina Sohail-621021-Base Fibonacci

def get_fibonacci (nterms):
    """Returns nterms Fibonacci number in the sequence
    
    Args:
                nterms(int): The number used to limit the size of the sequence
                Assumptions: nterms > 0
    
    Returns:
                fib[-1](int): The nterms of  the fibonacci sequence
    """
    n1, n2 = 0, 1
    count = 0
    fib = []
    
    print("Fibonacci sequence:")
    while (count < nterms):
        nth = n1 + n2

        n1 = n2
        n2 = nth
        fib = fib + [nth]
        count += 1
    return fib[-1]


def convert_decimal (num):
    """Converting a base fibonacci into a decimal number
    
    Args:
                num(str): Base fibonacci that will be converted
    
    Returns:
                final(int): The decimal number
    """
                
    n1 = 1
    n2 = 1
    count = 0
    final =0
    fib = []
    
    while (count <= len(num)):
        fib = fib + [n1]
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    fib.remove(fib[0])

    for a in range (len(num)):
        if (num[a-1] == '1'):
            final = final + fib[-a]
    return final

    
def get_option (n):
    """Getting an option from the user

        Args:
                    n(int): The number of options
                    Assumptions: n >  0
        
        Returns:
                    opt(int): Option choosen by user
        """
    while (True):
        try:
            opt = int(input("Enter your option: "))
            if opt in range (1, n+1):
                break
            else:
                print ("Pick one of the options")
        except:
            print ("Pick one of the options")
    return opt
            
def get_positive_integer (opt):
    """Using opt get a number from the user that is specified for the option

        Args:
                    opt(int): Option picked from user
                    Assumptions: opt > 1, opt < 4
                    
        Returns:
                    num(int): A number that will be converted to fibonacci
                    num(str): A Base Fibonacci that will be converted to decimal
        """
    while (True):
        try:
            if (opt == 1):
                num = str(input("Enter a base fibonacci: "))
                return num
            elif (opt == 2):
                num = int(input("Enter a number: "))
                return num
            if (num > 0):
                break
            else:
                print ("Enter a number greater than zero")
        except:
            if (opt != 3):
                print ("Please enter a number")
            else:
                break     

def print_menu ():
    print ('''Welcome to Base Fibonacci
    1. Convert Decimal to Fibonacci
    2. Convert Base Fibonacci to Decimal
    3. Quit''')

def main ():
    print_menu ()
    opt = get_option (3)
    num = get_positive_integer (opt)
    while (True):
        if (opt == 1):
            print(convert_decimal (num))
        elif (opt == 2):
            print(get_fibonacci (num))
        elif (opt == 3):
            break
        opt = get_option (3)
        num = get_positive_integer (opt)
        
main ()





