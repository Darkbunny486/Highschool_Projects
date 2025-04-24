
#c)
'''
word = input("Enter a word that only contains As and Bs: ")

while (True):
    word = input("Enter a word that only contains As and Bs: ")
    if (word.isalpha()):
        alpha  = True
    else:
        print ("Please use a word that only contains As and Bs")
    if (word.startswith("As")) or (word.startswith("Bs")):
        if (word.endswith("As")) or (word.endswith ("Bs")):
            if (alpha == True):
                break
            
word = word.lstrip ("As")
word = word.rstrip("As")
print(word)
'''
    