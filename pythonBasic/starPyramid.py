for i in range(1, 6):
    a = '*' * i
    print(a)

ans1 = int(input('start:\n'))
ans2 = int(input('end:\n'))
for i in range(ans1, ans2+1):
    a = '*' * i
    print(a)

print('--')

for i in range(ans1, ans2+1):
    a = '*' * i
    print(a)
for i in range(1, ans2 - ans1 + 1):
    a = '*' * (ans2 - i)
    print(a)

# import time
# while True:
#     for i in range(0, ans2 + 1):
#         a = '*' * i
#         print(a)
#         time.sleep(0.5)
#     for i in range(1, ans2):
#         a = '*' * (ans2 - i)
#         print(a)
#         time.sleep(0.5)


for i in range(1, 6):
    x = 2*(6 - i) -1
    a = '*' * x
    b = ' ' * int(((9 - x) / 2))
    print(b + a +b)

for i in range(ans1, ans2 +1):
    x = 2*i -1
    a = '*' * x
    b = ' ' * int(((2 * ans2 - 1 - x) / 2))
    print(b + a +b)

for i in range(1, ans2 - ans1 + 2): #끝 줄부터 시작 줄까지
    x = 2*(ans2 + 1 - i) -1
    a = '*' * x
    b = ' ' * int(((2 * ans2 - 1 - x) / 2))
    print(b + a + b)