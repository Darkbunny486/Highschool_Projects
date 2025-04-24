#1
'''
sentence = input("Enter a sentence: ")
words = sentence.split()
alpha = 0
num = 0

for word in words:
    if (word.isalpha()):
        alpha += 1
    elif (word.isdigit()):
        num += 1
        
print ("Number of words comprised of letters:", alpha)
print ("Number of words comprised of digits:", num)
'''
#2
'''
def isPalindrome (word):
    count = 0
    half = (len(word))//2
    for a in range (half):
        if (word[a] == word[-a-1]): #Checking if letters are the same
            count += 1
        else:
            break
    if (count == half):
        return True
    else:
        return False
        
def main ():
    sentence = input("Enter a sentence: ")
    words = sentence.split ()
    count = 0
    
    for word in words:
        pal = isPalindrome (word)
        count += 1
        if (pal == True):
            print ("Word", count, "is a palindrome")
        else:
            print ("Word", count, "is not a palindrome.")

main ()
'''
#3
'''
long = None
short = None
sentence = input("Enter a sentence: ")
words = sentence.split()

for word in words:
    if (long == None) and (short == None):
        long = len(word)
        long_word = word
        short = len(word)
        short_word = word
    elif (len(word) > long):
        long = len(word)
        long_word = word
    elif (len(word) < short):
        short = len(word)
        short_word = word

print ("Shortest word:", short_word)
print ("Longest word:", long_word)
'''