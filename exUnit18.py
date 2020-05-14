#while문 break 반복문 끝내기
i = 0
while True: 
    print(i)
    i += 1          
    if i == 10:   
        break

#for문 break 반복문 끝내기
for i in range(10000):   
    print(i)
    if i == 10:
        break

#for에서 continue로 코드 실행 건너뛰기
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#while 반복문에서 continue로 코드 실행 건너뛰기
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
