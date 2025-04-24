from math_utilities import *
from input_utilities import *

def main ():
    user = input("Would you like to play? (y/n)\n")
    while (user == 'y'):
        n = get_postive (False)
        m = get_postive (False)
        gcd2 = gcd (n, m)
        print(gcd2)
        user = input("Would you like to play again? (y/n)\n")
        
main ()