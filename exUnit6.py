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
