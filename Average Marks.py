mark = 0
average = 0
high = 0
low = 101
m = 0
n =0
while (m != -1):
    n = n + 1
    
    try:
        mark = int(input("Enter your mark: "))
    except:
        print ("That wasn't even a number, nevermind your mark!!!")
        mark = int(input("Enter your mark: "))
    
    if (mark >= 0) and (mark <= 100):
        average = average + mark
        if (mark > high):
            high = mark
        elif (mark < low):
            low = mark
    else:
        if (mark == -1):
            m = -1
        print ("invalid mark")
        n = n - 1

average = average/n
print ("Average Mark:", round(average, 2))
print ("Highest Mark:", high)
print ("Lowest Mark:", low)
