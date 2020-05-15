#차원 리스트를 만들고 요소에 접근하기
a = [[10,20],[30,40],[50,60]]
print(a)

#차원 리스트의 요소에 접근하기
print(a[0][0])
print(a[1][1])
print(a[2][1])
a[0][1] = 1000
print(a[0][1])

#톱니형 리스트
a = [[10,20],
     [500,600,700],
     [9],
     [30,40],
     [8],
     [800,900,1000]]
print(a)

a = []
a.append([])
a[0].append(10)
a[0].append(20)
a.append([])
a[1].append(500)
a[1].append(600)
a[1].append(700)
print(a)

#2차원 튜플
a = ((10,20),(30,40),(50,60))
b = ([10,20],[30,40],[50,60])
c = [(10,20),(30,40),(50,60)]
print(a, b, c, sep="/")

#사람이 알아보기 쉽게 출력하기
a = [[10, 20], [30, 40], [50, 60]]
print(a)

from pprint import pprint
pprint(a, indent=4, width=20)

#반복문으로 2차원 리스트의 요소를 모두 출력하기
a = [[10,20],[30,40],[50,60]]
for x,y in a:
    print(x,y)

for i in a:
    for j in i:
        print(j, end= ' ')
    print()

a = [[10,20],[30,40],[50,60]]

i = 0
while i < len(a):
    x, y = a[i]
    print(x,y)
    i += 1

#for 반복문으로 1차워 리스트 만들기
a = []

for i in range(10):
    a.append(0)
print(a)

a =  []
for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)
print(a)

a = [[0 for j in range(2)] for i in range(3)]
print(a)

a = [3,1,3,2,5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
print(b)

a = [[10,20],[30,40]]
b = a.copy()
b[0][0] = 500
print(a,b)

a = [[10,20],[30,40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
print(a,b)

