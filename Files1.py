#2
'''
file = open("She_Sells_Seashells.txt", "r")
outfile= open("OppOfSheSells.txt", "w")
count = 0

lines = file.readlines ()

    
for a in range (1, len(lines)):
    outfile.write (lines[len(lines)-a])
outfile.write (lines[0])    

outfile= open("OppOfSheSells.txt", "r")
print (outfile.read())


file.close ()
outfile.close ()
'''
#3
'''
file = open("She_Sells_Seashells.txt", "r")
lines = file.readlines ()
for line in lines:
    if "snake" in line:
        print (line)
'''
#4
'''
file = open("She_Sells_Seashells.txt", "r")
lines = file.readlines()
filenew = open("New.txt", "w")
count = 0
for line in lines:
    if count == 0:
        filenew.write ("1234 " + line)
        count += 1
    else:
        filenew.write (line)
filenew = open("New.txt", "r")
print (filenew.read())
'''
#5
'''
file = open("New.txt", "r")
lines = file.readlines()
lines[0] = lines[0].replace("1234 ", "")
print (lines)
'''
#6
'''
def linecount (filename):
    lines = filename.readlines ()
    return len(lines)

def wordcount (filename):
    count = 0
    lines = filename.readlines ()
    for line in lines:
        words = line.split ()
        count += len(words)
    return count    

def charcount (filename):
    count = 0
    lines = filename.readlines ()
    for line in lines:
        count += len(line)
    return count

file = open("She_Sells_Seashells.txt", "r")
print(linecount (file))
file = open("She_Sells_Seashells.txt", "r")
print(wordcount (file))
file = open("She_Sells_Seashells.txt", "r")
print(charcount (file))
'''