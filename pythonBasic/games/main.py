from pythonBasic.games.HangMan import runHangMan
from pythonBasic.games.updown import runUpDown
from pythonBasic.games.game2048 import run2048

def menuPrint():
    print('========GAME========')
    print('1.행맨')
    print('2.업다운')
    print('3.2048')
    print('0.종료')
    print('====================')


user_Input = -1
while user_Input != '0':
    menuPrint()
    user_Input = input('select menu\n')
    if user_Input == '1':
        runHangMan()
    elif user_Input == '2':
        runUpDown()
    elif user_Input == '3':
        run2048()