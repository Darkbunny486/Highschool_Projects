#Arina Sohail - 621021 - Unit 4 Assignment - Quiz Maker 2.0
#Lets users answer questions stores the grade in a dictionary and gives the average grade at the end when exiting the game

#Variables used in Program
gradesDiction = {}
num_grade = 0
totalGrade = 0
gradeCount = 0
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num_add = 0
import random

class Options:
    #gets a option number
    def num_options (self, max_num):
        while (True):#Check that it is a number 1 and the max number of options
            try:
                user = int(input("Enter a number: "))
                if (user >= 1) and (user <= max_num):
                    break
                else:
                    print ("Enter one of the options (1 to", str(max_num) +")")
            except:
                print ("Enter one of the options (1 to", str(max_num) +")")
        return user
        
    #Gets the user answers
    def answer (self):
        while (True):#Makes sure user_answer equals either A, B, C or D
            try:
                user_answer = input("Enter your answer: ")
                user_answer = user_answer.upper()
                if (user_answer == "A") or (user_answer == "B") or (user_answer == "C") or (user_answer == "D"):
                    break
                else:
                    print ("Enter the answer, either A, B, C or D.")
            except:
                print ("Enter the answer, either A, B, C or D.")
        return user_answer
        
    #Ask for conformation from the user
    def conformation (self):
        while (True): #Makes sure ask equals Y or N
            try:
                ask = input("Enter Y or N: ")
                ask = ask.upper()
                if (ask == "Y") or (ask == "N"):
                    break
                else:
                    print ("Please enter Y for yes or N for no.")
            except:
                print ("Please enter Y for yes or N for no.")
        return ask
    
option = Options()

class Grades:
    
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade
        
    @property
    def grades (self): #Used to print the grades
        return str(gradesDiction).replace("{","").replace("}","").replace("\'","")

    #Saves grades to a dictionary
    @grades.setter
    def grades (self, grade):
        name, grade = grade.split()#Saving name and grade
        if (gradesDiction != {}):#Making sure the dictionary isn't empty
            for key in gradesDiction:#Making sure there aren't same names because else it won't add to dictionary
                if (name == key):
                    while (True):
                        try:
                            print ("Spaces in your name will be taken out")
                            name = input("Please enter another name, this one is taken: ")
                            name = name.replace (" ", "")#Replaced spaces to make the first line in this function works
                            break
                        except:
                            print ("Enter a name, please")#Making sure the name works
        #Saving name and grade
        self.name = name
        self.grade = int(grade)
        gradesDiction[self.name] = self.grade#Adding name and grade to dictionary
        Grades.checkingNumGrades ()
    
    def __add__ (self, other):#Adding grades to find average
        global num_add
        listGrades = list(gradesDiction.items())
        if (diction == diction):#Making sure I only add each grade once
            if (num_add > 0):
                num_add += 2
            else:
                num_add += 1
            result = self.grade + listGrades[num_add-1][1]#Making sure I add two different grades
            return result
        else:
            if (num_add > 0):
                num_add += 2
            else:
                num_add += 1
            return (self.grade + other.grade)

    def __eq__ (self, other):#Using the magic method to check if the grades equal
        if (self.grade == other.grade):
            return True
        else:
            return False
    
    def checkingNumGrades ():#Adds grades, and finds the total number of grades to find the average grade
        #making sure I can access the variables
        global totalGrade
        global num_grade
        global gradeCount

        num_grade += 1
        gradeCount += 1#Counting the number of grades
        if (num_grade == 2):#Making sure I only add each grade once
            if (diction == diction):
                listGrades = list(gradesDiction.items())#Making sure the first grade is added instead of the second one being added twice
                TwoGrades = diction + listGrades[num_add-2][1]
            else:
                #adding the grades
                TwoGrades = (diction + diction)
            if (TwoGrades != None):
                totalGrade += TwoGrades
            num_grade = 0
            
    @classmethod
    def setAverageGrade (cls, totalGrade, gradeCount):#Saving average grade
        cls.averageGrade = totalGrade//gradeCount

#Uses option function and class to have player choose what they want to do
def play ():
    print ('''\n1. Start a New Quiz
2. Back to Main Menu''')
    opt = option.num_options(3)
    if (opt == 1):
        do_quiz ()
    else:
        menu.main_menu ()

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
                answer = option.answer()
                answer = answer + "\n"
                #Seeing if the player's answer is correct
                if (answer == real_ans):
                    print ("Correct!!")
                    correct += 1
                else:
                    print ("Incorrect")
        print ("Any spaces in your name will be taken out")
        name = input("Enter your name: ")
        name = name.replace (" ", "")
        grade = round((correct/orig_num_quest)*100)#Calculating the player's grade
        #*******************************************************New************************************************
        diction = Grades (name, grade)#Saves grades through a function
        diction.grades = name + " " + str(grade)
        #************************************************************************************************************
        print ("Your grade was " + str(grade) + "%.")
    else:
        print ("You must add more questions as this quiz has an inefficient number of questions")
    play ()#Returning the play menu

class Question:
    def __init__ (self, quiz):
        self.quiz = quiz

class addQuestion (Question):
    def add_question ():#adds question
    
        #getting question from user
        question = input("Add the text for the question you would like to add. Press enter when done.\n")
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
        add = option.conformation()
        if (add == "Y"):
            #adding question to file
            quiz.write ("\n" + question)
            quiz.write ("\n(A) " + A)
            quiz.write ("\n(B) " + B)
            quiz.write ("\n(C) " + C)
            quiz.write ("\n(D) " + D)
            quiz.write ("\n"+ answer + "\n")
                
        quiz.close()
        create ()
        
class delQuestion (Question):
    def delete_question ():#deletes question
        quizlist = quiz.readlines ()
        delete = input('''To delete a question, you will need to enter a key phrase to search for in the database.
    The first qusetion to contain this key phrase will be deleted. Press enter when done.\n''')
        for a in range (0, len(quizlist), 7):#Skips through the quiz to find the questions
            del_quest = quizlist[a].find (delete)#Finding the keyword in the questions
            if (del_quest != -1):
                question = quizlist[a]#Saves the question the player wants to delete
                del_num = a
                break
        if (del_quest == -1):#If there is no match for the key phrase, then it tells the user to
            print ('''Sorry, no question matches your key phrase to search for in the database.
    No question was deleted.''')
        else:
            print ("Match found:", question)
            #Asks for conformation if the player wants to delete the question
            conformation = option.conformation()
            if (conformation == "Y"):
                #Delete the question in the list
                for a in range (6):
                    del quizlist[del_num]
                del quizlist[del_num-1]
                #Updates the quiz to be replaced by quizlist
                quiz = open("quiz.txt", "w")
                for line in quizlist:
                    quiz.write (line)
                print ("Question deleted.")
            
        quiz.close ()
        create ()
        
#Shows create menu
#Uses option function to have player choose what they want to do
def create ():
    print ('''\n1. Add Question
2. Delete Question
3. Back to Main Menu''')
    opt = option.num_options (3)
    if (opt == 1):
        question = Question(open("quiz.txt", "a"))
        addQuestion.add_question ()
    elif (opt == 2):
        question = Question(open("quiz.txt", "r"))
        delQuestion.delete_question ()
    else:
        menu.main_menu ()

#Calculates average grade when exiting the quiz
def leave ():
    global totalGrade
    global gradeCount
    #Making sure I add the last grade in when number of grades of uneven
    if (len(gradesDiction)%2 != 0) and (gradeCount == len(gradesDiction)):
        listGrades = list(gradesDiction.items())
        listGrades[-1] = str(listGrades[-1]).upper()
        for letter in alpha:
            listGrades[-1] = listGrades[-1].replace(letter, '')#removing the name from the grade
        listGrades[-1] = listGrades[-1].replace ('\', ', '').replace('(\'', '').replace(')', '')
        totalGrade += int(listGrades[-1])#Changing the grade into a integer
    averageGrade = Grades.setAverageGrade(totalGrade, gradeCount) #Calculting the average grade
    print ("Average Grade: " + str(Grades.averageGrade) + "%")

class main_menu ():
     #Shows Main Menu   
    def main_menu (self):
        print ('''\n1. Play
2. Create
3. Exit''')
        opt = option.num_options(3)#Gets option from option class and function
        if (opt == 1):
            play ()
        elif (opt == 2):
            create ()
        else:
            leave ()
menu = main_menu ()
menu.main_menu ()
        
quiz = open("quiz.txt", "r")