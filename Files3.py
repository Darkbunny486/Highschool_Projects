import string

pathOne = "C:\\Users\\khize\\Desktop\\Python\\Notepad Files\\JKRowling1.txt"
pathTwo = "C:\\Users\\khize\\Desktop\\Python\\Notepad Files\\JKRowling2.txt"

file_one = open(pathOne, "r")
file_two = open(pathTwo, "r")

words = []
for line in file_one:
    words.append(line.split())
for line in file_two:
    words.append(line.split())
    

count = 0
sentence = ""
list_of_sentences = []
for lists in words:
    for word in lists:
        sentence = sentence + (word + " ")
        for letter in word:
            if (letter == "."):
                stop = True
            else:
                stop = False
        if (stop == True):
            list_of_sentences.append(sentence)
            sentence = ""


def mean_num_words (sentence_list):
    mean = 0
    for sentence in sentence_list:
        words = sentence.split()
        for word in words:
            if (word == "unusual") or (word == "hated") or (word == "Pointless"):
                mean  += 1
    return mean

def strip_sentence (sentence):
    for punctuation in string.punctuation:
        sentence = sentence.replace (punctuation, "")
    sentence = sentence.replace(" ", "")
    print (sentence)
        
for sentence in list_of_sentences:
    strip_sentence (sentence)




#print (mean_num_words(list_of_sentences))