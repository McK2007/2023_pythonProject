# number = 0
#
# while number < 10:
#     print(number)
#     number += 1
#
# print('====메뉴====\n', '1. 시작하기\n', '2. 종료하기\n', '==============')
#
# user_input = -1
#
# while True:
#     print('====메뉴====\n', '1. 시작하기\n', '2. 종료하기\n', '==============')
#     user_input = int(input())
#     if user_input == 2:
#         break

import random

answer = random.randrange(0, 10)
user_input = -1
# 사용자가 answer 맞출때까지 반복
# 1. 사용자에게 기회주기
# 2. 틀렸을때 updown 출력해주기
chance = 3

while True:
    user_input = int(input())
    if answer == user_input:
        print('correct')
        break
    else:
        chance -= 1
        if chance == 0:
            print('game_over')
            break
        print('chance:', chance)
        print('try again')
        if user_input < answer:
            print('up')
        else:
            print('down')