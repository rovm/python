#리스트와 튜플 사용하기
a = 10
b = 20
print(a, b, sep=',')

a = [38, 21, 53, 62, 19]
print(a)

#리스트에 여러가지 자료형 저장하기
person = ['james',17 ,175.3 ,True]
print(person)

#빈 리스트 만들기
a = []
print(a)
b =list()
print(b)

#range를 사용하여 리스트 만들기
print(range(10))
a = list(range(10))
print(a)

b = list(range(5,12))
print(b)

c = list(range(-4, 10, 2))
print(c)

d = list(range(10, 0, -1))
print(d)

#튜플 사용하기
a = (38, 21, 53, 62, 19)
print(a)

a = 38, 21, 53, 62, 19
print(a)

person = ('james', 17, 175.3, True)
print(person)

#range를 사용하여 튜플 만들기
a = tuple(range(10))
print(a)

b = tuple(range(5, 12))
print(b)

c = tuple(range(-4, 10, 2))
print(c)

#튜플을 리스트로 만들고 리스트를 튜플로 만들기
a = [1, 2, 3]
print(tuple(a))

b = (4, 5, 6)
print(list(b))

print(list('Hello'))
print(tuple('Hello'))
a, b, c = [1, 2, 3]
print(a, b, c)
d, e, f = (4, 5, 6)
print(d, e, f)

#x = input().split()
#a, b = x
#print(a, b)

print(list(range(5, -10, -2)))
