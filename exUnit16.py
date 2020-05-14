#for와 range 사용하기
for i in range(10):
    print(i)

#for와 range 응용하기
for i in range(5,12):
    print(i)

#증가폭 사용하기
for i in range(0, 10, 2):
    print(i)

#숫자를 감소시키기
for i in range(10, 0, -1):
    print('감소:', i)

#시퀀스 객체로 반복하기
a = [10, 20, 30, 40, 50]

for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')    
for i in fruits:
    print(i)

for letter in 'Python':
     print(letter, end=' ')
print('\n')
for letter in reversed('Python'):
     print(letter, end=' ')
