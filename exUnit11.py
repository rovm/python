#특정 값이 있는지 확인하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(30 in a)
print(100 in a)
print(100 not in a)
print(30 not in a)

print(43 in (38, 76, 43, 62, 19))
print(1 in range(10))
print('P' in 'Hello, Python')

a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
print(a + b)

print([0, 10, 20, 30] * 3)

print('Hello, ' * 3)

#리스트와 튜플의 요소 개수 구하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(len(a))

b = (38, 76, 43, 62, 19)
print(len(b))

print(len(range(0, 10, 2)))
hello = 'Hello, world!'
print(len(hello))

#인덱스 요소 사용하기
b = (38, 21, 53, 62, 19)
print(b[0])

r = range(0, 10, 2)
print(r[2])

hello = 'Hello, world!'
print(hello[7])

a = [38, 21, 53, 62, 19]
print(a[-1])
print(a[-5])

r = range(0, 10, 2)
print(r[-3])

hello = 'Hello, world!'
print(hello[-4])

a = [0, 0, 0, 0, 0]
a[0] = 38
a[1] = 25
a[2] = 35
a[3] = 64
a[4] = 74
print(a)

#del로 요소 삭제 하기
del a[2]
print(a)
