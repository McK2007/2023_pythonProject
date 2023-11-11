def runUpDown():
    import random

    answer = random.randrange(0, 10)
    chance = 3

    while chance > 0:
        user_input = input()
        if user_input.isnumeric():
            user_input = int(user_input)
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