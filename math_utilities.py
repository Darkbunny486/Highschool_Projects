def num_diag (n):
    """Determine the number of diafonals in an n-sided polygon
    
    Args:
            n(int): Number of sides of the polygon
            Assumptions: n > 2
            
    Returns:
            d(int): Number of diagonals
    """
    d = n*(n - 3)/2
    return d

def sum_cubes (n):
    """Determining the cube of n
    
    Args:
        n(int): Number that will be cubed
    
    Returns:
        cube(int): The cube of n
    """
    cube = n**3
    return cube

def sum_even (n):
    """Determine the sum of the even numbers smaller than n
    
    Args:
        n(int): Number to stop at
        Assumption: n > 0
        
    Returns:
        even(int): Sum of the even numbers
    """
    even = 0
    for a in range (n):
        if ((a % 2) == 0):
            even = even + a
    return even

def sum_odd (n):
    """Determine the sum of the odd numbers smaller than n
    
    Args:
        n(int): Number to stop at
        Assumption: n > 0
        
    Returns:
        odd(int): Sum of the odd numbers
    """
    odd = 0
    for a in range (n):
        if ((a % 2) != 0):
            odd = odd + a
    return odd

def approximate_pi (n):
    """Gives an approximation of pi
    
    Args:
            n(int): Number of how accurate you would like the approximation
            Assumptions: n > 0
            
    Returns:
            total(int): The approximation of pi
    """
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total -= 4/(2*i - 1)
        else:
            total += 4/(2*i - 1)
    return total

def find_factors (n):
    """Determines the factors of n
    
    Args:
        n(int): Number to find factors of
        Assumptions: n > 0
    
    Returns:
        factors(list): List of the factors of n
    """
    factors = []
    for a in range (1, n+1):
        if ((n%a) == 0):
            factors = factors + [a]
    return factors

def factorials (n):
    """Finding the factorial of n
    
    Args:
            n(int): The number you are changing into a factorial
            Assumption: n > 0
    
    Returns:
            total(int): The factorial of n
    """
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def is_even (n):
    """Determine if n is even

    Args:
        n(int): The number to determine if even
    
    Returns:
        even(boolean): Tell if n is even
    """
    if ((n%2) == 0):
        even = True
    else:
        even = False
        return even
    
def is_prime (n):
    """Determining if n is prime

    Args:
        n(int): The number to determine if prime
        Assumption: n > 0
        
    Returns:
        prime(boolean): Tell if n is prime
    """
    factors = 0
    for a in range (1, n+1):
        if ((n%a) == 0):
            factors = factors + 1
    if (factors == 2):
        prime = True
    else:
        prime = False
    return prime

def gcd (n, m):
    """Determining the greatest common denominator of n and m

    Args:
            n(int): An integer
            m(int): Another integer
            Assumptions: n > 0, m > 0
            
    Returns:
            d(int): The greatest common denominator of n and m
    """
    if (n > m):
        for a in range (1, n):
            if ((n % a) == 0) and ((m % a) == 0):
                d = a
    else:
        for a in range (1, m):
             if ((n % a) == 0) and ((m % a) == 0):
                d = a       
    return d


def main ():
    print(is_prime (5))
    
if __name__ == '__main__':
    main ()