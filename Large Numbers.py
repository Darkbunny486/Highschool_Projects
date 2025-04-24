num = 1
large = 0
largetwo = 0

while (num > 0):
    e = True
    while (e == True):
        try:
            num = int(input("Enter a number: "))
            e = False
        except:
            print ("That wasn't a number!!")
    if (num > large):
        largetwo = large
        large = num 
    elif (num > largetwo):
        largetwo = num
print ("Largest Number:", large)
print ("Second Largest Number:", largetwo)
