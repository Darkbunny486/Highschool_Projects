#Pig_Latin

def main ():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence = ""
    count = 0
 
    for word in words:

        if word[0] in vowels:
            word = word + "hay"
            count += 1
            
        else:
            letter2 = word[0]
            word = word.replace(word[0], "")
            word = word + letter2 + "hay"
            count += 1

        if (count == 1):
            sentence = sentence + word
        else:
            sentence = sentence + " " +  word
    print (sentence)
    

main()