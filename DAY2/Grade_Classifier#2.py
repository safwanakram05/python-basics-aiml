x = int(input('Enter your math score out of 100..\n'))

if x >= 111:
    print('Wrong input')
elif x >= 90 <= 100:
    print('A+')
elif x >= 80 <= 89:
    print('A')
elif x >= 70 <= 79:
    print('C')
elif x >= 60 <= 69:
    print('D')
else:
    print('FAIL!')