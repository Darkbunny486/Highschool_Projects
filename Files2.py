#1
'''
path = "C:\\Users\\khize\\Desktop\\Python\\Notepad Files/studentdata.txt"
infile = open(path , "r")
'''
#a)
'''
for line in infile:
    words = line.split()
    testScores = words
    testScores.pop(0)
    if (len(testScores) > 6):
        print (testScores)
'''
#b)
'''
for line in infile:
    words = line.split()
    testScores = words.copy()
    testScores.pop(0)
    total = 0
    numTests = 0
    for score in testScores:
        total += int(score)
        numTests += 1
    print (words[0] + ":", round(total/numTests, 1))
'''
#c)
'''
for line in infile:
    words = line.split()
    name = words[0]
    testScores = words
    testScores.pop(0)
    lowScore = min(testScores)
    highScore = max(testScores)
    print (name)
    print ("Lowest Score:", lowScore)
    print ("Highest Score:", highScore)
'''
#2

path = "C:\\Users\\khize\\Desktop\\Python\\Notepad Files/qbdata.txt"
infile = open(path , "r")

#a)
'''
for line in infile:
    words = line.split ()
    print (words[0], words[1], "has a rating of", words[10])
    
infile.close ()
'''
#b)
'''
for line in infile:
    words = line.split ()
    print (words[1] + ",", words[0])
    
infile.close()
'''
#c)
'''
rates = []
names = []
for line in infile:
    words = line.split ()
    names = names + [words[0] + " " + words[1]]
    rates = rates + [words[10]]
    
maxRate = max(rates)
maxIndex = rates.index(maxRate)
print ("Highest Rate:", maxRate)
print (names[maxIndex])
'''
#d)
'''
for line in infile:
    words = line.split ()
    average = int(words[7])/int(words[4])
    print (words[0], words[1], average)
'''
#e)
'''
for line in infile:
    words = line.split ()
    comp = int(words[4])
    if (comp > 300):
        print(comp)
'''