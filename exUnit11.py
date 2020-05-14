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

#슬라이스 사용하기
a = [0,10,20,30,40,50,60,70,80,90]
print(a[0:4])
print(a[0:10])
print(a[1:0])
print(a[1:2])

#리스트의 중간 부분 가져오기
print(a[4:7])
print(a[4:-2])
print(a[2:8:3])
print(a[2:9:3])
print(a[:7])
print(a[7:])
print(a[:])
print(a[0:7:2])
print(a[7::2])
print(a[::2])

#len 응용하기
print(a[0:len(a)])
print(a[:len(a)])

#튜플 range 문자열에 슬라이스 적용하기
b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
print(b[4:7])
print(b[4:])
print(b[:7:2])

r = range(10)
print(r[0:10])
print(r[4:7])
print(r[4:10])
print(r[:7:2])
print(list(r[:7:2]))

hello = 'Hello, world!'
print(hello[2:9])
print(hello[2:])
print(hello[:9:2])

#슬라이스에 요소 할당하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
#a[2:5] = ['a','b','c']
#a[2:5] = ['a']
#a[2:5] = ['a','b','c','d']
#a[2:8:2] = ['a','b','c']
#del a[2:5]
del a[2:8:2]
print(a)
