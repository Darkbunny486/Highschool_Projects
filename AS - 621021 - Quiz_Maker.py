#Arina Sohail - 621021 - Quiz_Maker
import time
import random

#Shows main menu
#Lets player choose to edit or play the quiz
def main_menu ():
    print ('''\n1. Play
2. Create
3. Exit''')
    opt = option (3)
    if (opt == 1):
        play ()
    elif (opt == 2):
        create ()
    
def option (num_opt):
    """Takes a number from the player to know what the player wants to do

    Args:
            num_opt(int): The limit of the number of options
            Assumptions: num_opt > 1
            
    Returns:
            opt(int): The option the player choose
    """     
    while (True):
        try:
            opt = int(input("Enter your option: "))
            if (opt < 1) or (opt > num_opt):
                print ("Please enter one of the options")
            else:
                break
        except:
            print ("Please enter one of the option numbers")
    return opt

#Shows play menu
#Uses option function to have player choose what they want to do
def play ():
    print ('''\n1. Start a New Quiz
2. Back to Main Menu''')
    opt = option (2)
    if (opt == 1):
        do_quiz ()
    else:
        main_menu ()

#Shows create menu
#Uses option function to have player choose what they want to do
def create ():
    print ('''\n1. Add Question
2. Delete Question
3. Back to Main Menu''')
    opt = option (3)
    if (opt == 1):
        add_question()
    elif (opt == 2):
        delete_question()
    else:
        main_menu ()

#Lets player play through the quiz 
def do_quiz ():
    quiz = open("quiz.txt", "r")
    quizlist = quiz.readlines()
    num_quest = round(len(quizlist)/7)#Counts the number of questions in the quiz
    orig_num_quest = num_quest#Keeps the number of questions at the start of the quiz
    quiz.close ()
    correct = 0
    if (num_quest >= 10):#Makes sure there are more than 10 questions in the quiz before starting
        for a in range (num_quest):
            while (True):
                num_quest = round(len(quizlist)/7)#Updates the amount of questions left
                if (len(quizlist) == 0) or (num_quest == 0):
                    break
                num = random.randint (1, num_quest)#Chooses a random question
                num = (num - 1)*7#Makes the question number into the line number the question is on
                for a in range (7):
                    #Prints the question, but not the answer, then deletes it from the list
                    if (quizlist[num] != "A\n") and (quizlist[num] != "B\n") and (quizlist[num] != "C\n") and (quizlist[num] != "D\n"):
                        print (quizlist[num])
                        del quizlist [num]
                    else:
                        real_ans = quizlist[num] #Saves the answer
                        del quizlist [num]#Deletes the answer from the list
                        break
                if (num < len(quizlist)):#Deletes the extra space if there is any
                    del quizlist[num]
                #Gets the players answer making sure they entered either A, B, C or D
                while (True):
                    try:
                        answer = input("Enter your answer: ")
                        answer = answer.upper ()
                        if (answer != "A") and (answer != "B") and (answer != "C") and (answer != "D"):
                            print ("Enter either A, B, C or D as your answer")
                        else:
                            break
                    except:
                        print ("Enter either A, B, C or D as your answer")
                answer = answer + "\n"
                #Seeing if the player's answer is correct
                if (answer == real_ans):
                    print ("Correct!!")
                    correct += 1
                else:
                    print ("Incorrect")
                time.sleep (1)
        grade = round((correct/orig_num_quest)*100)#Calculating the player's grade
        print ("Your grade was " + str(grade) + "%.")
    else:
        print ("You must add more questions as this quiz has an inefficient number of questions")
    play ()#Returning the play menu
    
def add_question ():
    
    #getting question from user
    question = input("Add the text for the question you would like to add. Press enter when done.\n")
    time.sleep (0.1)
    print ("Now enter the options for choice A, B, C, D. Press enter after each entry.")
    A = input ("(A) ")
    B = input ("(B) ")
    C = input ("(C) ")
    D = input ("(D) ")
    while (True):
        answer = input("Now enter the answer (A, B, C or D): ")
        answer = answer.upper ()
        if (answer == "A") or (answer == "B") or (answer == "C") or (answer == "D"):
            break
        else:
            print ("Please enter either A, B, C or D")
    
    #conformation to add the question to the file
    while (True):
        add = input("Would you like to add this question to the database (Y/N)?\n")
        add = add.upper ()
        if (add == "Y") or (add == "N"):
            break
        else:
            print ("Please enter either Y or N")
    if (add == "Y"):
    
        #adding question to file
        quiz = open("quiz.txt", "a")
        quiz.write ("\n" + question)
        quiz.write ("\n(A) " + A)
        quiz.write ("\n(B) " + B)
        quiz.write ("\n(C) " + C)
        quiz.write ("\n(D) " + D)
        quiz.write ("\n"+ answer + "\n")
            
    quiz.close()
    create ()

def delete_question ():
    quiz = open("quiz.txt", "r")
    

#The main function
#Starts the program
def main ():
    main_menu ()
        
main ()
