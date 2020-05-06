#정수 계산하기
print(1 + 1) #2
print(1 - 2) # -1
print(5 / 2) # 2.5
print(4 / 2) # 2.0
print(5.5 // 2) # 2
print(4 // 2) # 2
print(4.1 // 2.1) # 1.0
print(5 % 2) # 1
print(2 ** 10) # 1024
print(int(3.3)) # 3
print(int(5/2)) # 2
print(int('10')) # 10
print(type(10)) # <class 'int'>
print(divmod(5,2)) # (2,1)

a, b = divmod(5,2)
print(a)
print(b)
print(a, b)

print(0b110) # 6
print(0o10) # 8
print(0xf) # 15
print("---------------------------------------------------------")

#실수 계산하기
print(3.5 + 2.1) # 5.6
print(5.3 - 2.7) # 2.5999999999999996
#근사값이 나옴 컴퓨터는 실수를 표현할때 오차 발생
print(1.5 * 3.1) # 4.65
print(5.5 / 3.1) # 17741935483870968
print(4.2 + 5) # 9.2
print(float(5)) # 5.0
print(float(1 + 2)) # 3.0
print(float('5.3')) # 5.3
print(type(3.5)) # <class 'float'>
print(1.2+1.3j) # (1.2+1.3j)
#수학에서는 허수는i 이지만 공학에서 허수는 j를 사용
print(complex(1.2, 1.3)) # (1.2+1.3j)
print("---------------------------------------------------------")

#괄호사용하기
print(35 + 1 * 2) # 37
print((35 + 1) * 2) # 72
