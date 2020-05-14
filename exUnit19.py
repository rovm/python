#계단식으로 별 출력하기
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print('')

print('------------------------------')
#사각형으로 별 출력하기
for i in range(5):
    for j in range(5):
        print('*', end='')
    print('')

print('------------------------------')
#대각선으로 별 출력하기
for i in range(5):
    for j in range(5):
        if(i == j):
            print('*', end='')
        else:
            print(' ', end='')
    print('')
