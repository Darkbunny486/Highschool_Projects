from random import *

def random_bday (n):
    """Returns a list of n integers randomly chosen
    between 1 and 365.

    Args:
            n(int): Number of days to generate
            Assumption: n >= 1

    Returns:
            bdayList(list): List of n integers between 1-365
    """
    bdayList = []
    for b in range (n):
        bday = randint (1, 365)
        bdayList = bdayList + [bday]
    return bdayList
   
   
def has_duplicates (bdayList):
    """Returns True if any element appears more than
    once in t, False otherwise.

    Args:
            bdayList(list): List of values

    Returns:
            bool: True or False
    """
    for b in range (23):
        for a in range (23):
            if (a != b):
                if (bdayList[b] == bdayList[a]):
                    dup = True
                    break
                else:
                    dup = False
                    
    return dup

def main ():
    for some in range (1000):
        bdayList = random_bday (23)
        dup = has_duplicates(bdayList)
        print (dup)
 
        
main ()
                
