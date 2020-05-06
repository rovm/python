#변수 만들기
x = 10
print(x)

y = 'Hello, World!'
print(y)

#변수의 자료형 알아내기
print(type(x))
print(type(y))

#변수 여러 개를 한 번에 만들기
x, y, z = 10 , 20 ,30
print('x = ', x, 'y = ', y, 'z = ', z)

x = y = z = 10
print('x = ', x, 'y = ', y, 'z = ', z)

x, y = 10, 20
x, y =  y, x
print('x = ', x, 'y = ', y)

#참고 변수 삭제
#x = 10
#del x
#print(x)

x = None #None = Null
print(x) 

#변수로 계산하기
a = 10
b = 20
c = a + b
print(c)

#산술 연산 후 할당 연산자 사용하기
a = 10
print(a + 20)
print(a)

a = 10
a = a + 20
print(a)

a = 10
a += 20
print(a)

#input 함수 사용하기


x = -10
print(+x)
print(-x)

#x = input()
# C언어의 scanf 같은 기능임

#두 숫자의 합 구하기
a = int(input('1번째 수'))
b = int(input('2번째 수'))
print(a+b)
print(type(a))
