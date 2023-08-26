number = 0

while number < 10:
    print(number)
    number += 1

print('====메뉴====\n', '1. 시작하기\n', '2. 종료하기\n', '==============')

user_input = -1

while True:
    print('====메뉴====\n', '1. 시작하기\n', '2. 종료하기\n', '==============')
    user_input = int(input())
    if user_input == 2:
        break
