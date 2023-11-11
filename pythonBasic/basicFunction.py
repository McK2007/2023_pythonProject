# def tmpFunction(x):
#     return 3*x +5
# x = int(input())
# print(tmpFunction(x))

# 게임

def menuPrint():
    print('========GAME========')
    print('1.행맨')
    print('2.업다운')
    print('0.종료')
    print('====================')

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
        if CorrectWord[i] == '_':
            if b[i].lower() == c:
                returnWord = returnWord + b[i]
            else:
                returnWord = returnWord + '_'
        else:
            returnWord  = returnWord + CorrectWord[i]
    return returnWord

def runHangMan():
    global hangman_input_history
    hangman_input_history = []
    word = getRandomWord()
    chance = 8
    global CorrectWord
    CorrectWord = '_' * len(word)
    countCorrect = 0
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


def runUpDown():
    import random

    answer = random.randrange(0, 10)
    chance = 3

    while chance > 0:
        user_input = int(input())
        if answer == user_input:
            print('correct')
            break
        else:
            chance -= 1
            if chance > 0:
                print('chance:', chance)
                print('try again')
                if user_input < answer:
                    print('up')
                else:
                    print('down')
            else:
                print('game_over')


user_Input = -1
while user_Input != 0:
    menuPrint()
    user_Input = int(input('select menu\n'))
    if user_Input == 1:
        runHangMan()
    elif user_Input == 2:
        runUpDown()
