from random import *
import random
cptchoices =  ["Rock", "Paper", "Scissors"]
user = str(input("Rock, Paper, or Scissors, Please one upper case letter:\n"))
cpt = random.choice(cptchoices)

print ("Computer:", cpt)
print ("Player:", user)

if (user == "Rock") and (cpt ==  "Paper"):
    print ("You Lose")
elif (user == "Rock") and (cpt ==  "Scissors"):
    print ("You Win")
elif (user == "Rock") and (cpt ==  "Rock"):
    print ("Tie")
elif (user == "Paper") and (cpt ==  "Rock"):
    print ("You Win")
elif (user == "Paper") and (cpt ==  "Scissors"):
    print ("You Lose")
elif (user == "Paper") and (cpt ==  "Paper"):
    print ("Tie")
elif (user == "Scissors") and (cpt ==  "Paper"):
    print ("You Win")
elif (user == "Scissors") and (cpt ==  "Rock"):
    print ("You Lose")
elif (user == "Scissors") and (cpt ==  "Scissors"):
    print ("Tie")
