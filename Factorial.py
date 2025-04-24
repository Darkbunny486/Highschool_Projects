try:
    n = int(input("Enter a number: "))
except:
    print ("That was not a number!!")
    n = int(input("Enter a number: "))
m = n
while (n > 1):
    m = m*(n - 1)
    n = n -1

print (m)
