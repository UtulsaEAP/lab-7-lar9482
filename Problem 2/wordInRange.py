"""
    Name: Luke Runnels
    Lab time: 3/8/2024
"""

def wordInRange():
    #Type your code here
    inputFileName = input()
    firstWord = input()
    secondWord = input()

    with open(inputFileName, "r") as file:
        fileWords = file.readlines()

        for word in fileWords:
            word = word.strip("\n")

            if (isInclusive(word, firstWord, secondWord)):
                print(f'{word} - in range')
            else:
                print(f'{word} - not in range')

def isInclusive(word, firstWord, secondWord):
    for i in range(0, len(word)):
        if (ord(word[i]) < ord(firstWord[i])):
            return False
        if (ord(word[i]) > ord(firstWord[i])):
            break
    
    for i in range(0, len(word)):
        if (ord(word[i]) > ord(secondWord[i])):
            return False
        if (ord(word[i]) < ord(secondWord[i])):
            break

    return True

if __name__ == '__main__':
    wordInRange()