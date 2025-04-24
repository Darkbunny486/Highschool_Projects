n = int(input("Enter a number: "))
fib1 = 1
fib2 = 1

for a in range (n):
    print (fib1, end=" ")
    temp = fib1
    fib1 = fib2
    fib2 = temp + fib1
