from random import *
import copy
def TicTacToe_Table ():
    start = 1
    finish = 3
    Alist = []
    table = []
    for a in range (3):
        for b in range (start, finish+1):
            Alist.append (b)
        table.append (Alist)
        my_table = copy.deepcopy(table)
        start += 3
        finish += 3
        Alist = []
    return table, my_table

def print_table (table):
    for a in range (len(table)):
        print (table[a])
        
def pick ():
    while (True):
        try:
            user = input("Which one would you like to be? (O/X)\n")
            if (user == "O"):
                comp = "X"
                break
            elif (user == "X"):
                comp = "O"
                break
            else:
                print ("Please enter O or X")
        except:
            print ("Please enter O or X")
    return user, comp
         
def play (user, comp, table, my_table):
    tryagain = 0
    while (True):
        try:
            usernum = int(input("Enter where you want your piece?\n"))
            if (usernum <= 3):
                my_table[0].pop (usernum-1)
                table[0].pop (usernum-1)
                table[0].insert (usernum-1, user)
                break
            elif (usernum <=6):
                my_table[1].pop (usernum-4)
                table[0].pop (usernum-4)
                table[0].insert (usernum-4, user)
                break
            elif (usernum <= 9):
                my_table[2].pop (usernum-7)
                table[0].pop (usernum-7)
                table[0].insert (usernum-7, user)
                break
            else:
                print ("Please enter a number avaliable")
        except:
            print ("Please enter a number avaliable")
    while (True):
        try:
            compnum = randint(1, 9)
            if (compnum <= 3):
                my_table[0].pop (compnum-1)
                table[0].pop (compnum-1)
                table[0].insert (compnum-1, comp)
                break
            elif (compnum <=6):
                my_table[1].pop (compnum-4)
                table[0].pop (compnum-4)
                table[0].insert (compnum-4, comp)
                break
            else:
                my_table[2].pop (compnum-7)
                table[0].pop (compnum-7)
                table[0].insert (compnum-7, comp)
                break
        except:
            tryagain += 1
    print (compnum)
    return table, my_table

def main ():
    table, my_table = TicTacToe_Table ()
    user, comp = pick ()
    while (True):
        win = None
        print_table (table)
        table, my_table = play (user, comp, table, my_table)
        if (table[0] == ["X", "X", "X"]):
            #X wins
            win = "X"
            break
        elif (table[1] == ["X", "X", "X"]):
            #X wins
            win = "X"
            break
        elif (table[2] == ["X", "X", "X"]):
            #X wins
            win = "X"
            break
        elif (table[0] == ["O", "O", "O"]):
            #O wins
            win = "O"
            break
        elif (table[1] == ["O", "O", "O"]):
            #O wins
            win = "O"
            break
        elif (table[2] == ["O", "O", "O"]):
            #O wins
            win = "O"
            break
        elif (table[0][0] == "O") and (table[1][1] == "O") and (table[2][2] == "O"):
            #O wins
            win = "O"
            break
        elif (table[0][0] == "X") and (table[1][1] == "X") and (table[2][2] == "X"):
            #X wins
            win = "X"
            break
        elif (table[2][0] == "O") and (table[1][1] == "O") and (table[0][2] == "O"):
            #O wins
            win = "O"
            break
        elif (table[2][0] == "X") and (table[1][1] == "X") and (table[0][2] == "X"):
            #X wins
            win = "X"
            break
        elif (table[0][0] == "O") and (table[1][0] == "O") and (table[2][0] == "O"):
            #O wins
            win = "O"
            break
        elif (table[0][0] == "X") and (table[1][0] == "X") and (table[2][0] == "X"):
            #X wins
            win = "X"
            break
        elif (table[0][1] == "O") and (table[1][1] == "O") and (table[2][1] == "O"):
            #O wins
            win = "O"
            break
        elif (table[0][1] == "X") and (table[1][1] == "X") and (table[2][1] == "X"):
            #X wins
            win = "X"
            break
        elif (table[0][2] == "O") and (table[1][2] == "O") and (table[2][2] == "O"):
            #O wins
            win = "O"
            break
        elif (table[0][2] == "X") and (table[1][2] == "X") and (table[2][2] == "X"):
            #X wins
            win = "X"
            break
        elif (table[0][0] != 1) and  (table[0][1] != 2) and (table[0][2] != 3) and (table[1][0] != 4) and (table[1][1] != 5) and (table[1][1] != 5) and (table[1][2] != 6)\
             and (table[2][0] != 7) and (table[2][1] != 8) and (table[2][2] != 9):
            #Tie
            break
    if (win == "X"):
        if (user == "X"):
            print ("You win")
        else:
            print ("You lost")
    elif (win == "O"):
        if (user == "O"):
            print ("You win")
        else:
            print ("You lost")
    else:
        print ("Tie")

main ()

