def getRandomWord():
    import random
    words = ['hang', 'pretty', 'apple', 'ant', 'water', 'samsung', 'MCdonalds', 'fluent', 'voca', 'galaxy']
    return words[random.randrange(0, len(words))]

hangman_input_history = []

def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if(user_input.isalpha()): #알파벳인지 확인
            alphabet = user_input[0].lower()
            if(alphabet in hangman_input_history): #이미 입력된 값인지 확인
                print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요.")
            else:
                return alphabet
                break

CorrectWord = ''
word = ''
def printCorrectWord(b, c):
    returnWord = ''
    for i in range(0, len(b)):
        if CorrectWord[2 * i] == '_':
            if b[i].lower() == c:
                returnWord = returnWord + b[i] + ' '
            else:
                returnWord = returnWord + '_ '
        else:
            returnWord  = returnWord + CorrectWord[2 * i] + ' '
    return returnWord

def runHangMan():
    global hangman_input_history
    hangman_input_history = []
    word = getRandomWord()
    chance = 8
    global CorrectWord
    CorrectWord = '_ ' * len(word)
    countCorrect = 0
    print(CorrectWord)
    while chance > 0:
        alphabet = getHangmanInput()
        hangman_input_history.append(alphabet)
        if word.find(alphabet) != -1 or word.find(alphabet.upper()) != -1:
            print('correct')
            countCorrect += word.count(alphabet)
            CorrectWord = printCorrectWord(word, alphabet)
            print(CorrectWord)
            if countCorrect == len(word):
                print('alive')
                break

        else:
            chance -= 1
            print('LEFT CHANCE: ', chance)

        # printStr = ''
        # for i in word:
        #     if i in hangman_input_history:
        #         printStr = printStr + i
        #     else:
        #         printStr = printStr +'_'
        #     printStr = printStr + ' '
        # print(printStr)