score = float(input('이번 시험의 점수를 입력하시오\n'))
if score >100 or score < 0:
    print('값을 잘못 입력하셨습니다')
elif score >= 90 :
    print('A반입니다')
elif score >= 80 :
    print('B반입니다')
elif score >= 70 :
    print('C반입니다')
elif score >= 60:
    print('D반입니다')
else:
    print('E반입니다')