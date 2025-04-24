from random import *

LetterOne = choice("ABCDEFGHIJKLMOPQRSTUVWXYZ")
LetterTwo = choice("ABCDEFGHIJKLMOPQRSTUVWXYZ")
LetterThree = choice("ABCDEFGHIJKLMOPQRSTUVWXYZ")

if (LetterOne == "A") or (LetterOne == "E") or (LetterOne == "I")\
   or (LetterOne == "O") or (LetterOne == "U"):

    if (LetterTwo == "A") or (LetterTwo == "E") or (LetterTwo == "I")\
       or (LetterTwo == "O") or (LetterTwo == "U"):
        print ("Two letters are vowels")
    if (LetterThree == "A") or (LetterThree == "E") or (LetterThree == "I")\
       or (LetterThree == "O") or (LetterThree == "U"):
        print ("Two letters are vowels")
        
elif (LetterTwo == "A") or (LetterTwo == "E") or (LetterTwo == "I")\
       or (LetterTwo == "O") or (LetterTwo == "U"):

    if (LetterOne == "A") or (LetterOne == "E") or (LetterOne == "I")\
       or (LetterOne == "O") or (LetterOne == "U"):
        print ("Two letters are vowels")
    if (LetterThree == "A") or (LetterThree == "E") or (LetterThree == "I")\
       or (LetterThree == "O") or (LetterThree == "U"):
        print ("Two letters are vowels")

elif (LetterThree == "A") or (LetterThree == "E") or (LetterThree == "I")\
     or (LetterThree == "O") or (LetterThree == "U"):
    
    if (LetterOne == "A") or (LetterOne == "E") or (LetterOne == "I")\
       or (LetterOne == "O") or (LetterOne == "U"):
        print ("Two letters are vowels")
    if (LetterTwo == "A") or (LetterTwo == "E") or (LetterTwo == "I")\
       or (LetterTwo == "O") or (LetterTwo == "U"):
        print ("Two letters are vowels")
        
else:
    print("There are no vowels")



    
    
