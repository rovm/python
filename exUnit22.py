#리스트에 요소 하나 추가하기
a = [10,20,30]
a.append(500)
print(a)
print(len(a))

a = []
a.append(10)
print(a)

a = [10,20,30]
a.append([500,600])
print(a)

a = [10,20,30]
a.extend([500,600])
print(a)

a = [10,20,30]
a.insert(2,500)
print(a)

a = [10,20,30]
a[1:1] = [500,600]
print(a)

#리스트에서 요소 삭제하기
#pop 마지막 요소 삭제
#remove 찾아서 요소 삭제


a = [10,20,30]
a.pop()
print(a)

a = [10,20,30]
a.pop(1)
print(a)

a = [10,20,30]
del a[1]
print(a)

a = [10,20,30,20]
a.remove(20)
print(a)

a = [10,20,30,15,20,40]
a.index(20)
print(a)

a = [10,20,30,15,20,40]
print(a.count(20))
a.reverse()
print(a)

a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)
a.clear
print(a)

a = [10,20,30]
del a[:]
print(a)

a = [10,20,30]
a[len(a):] = [500]
print(a)

#리스트의 할당과 복사 알아보기
a = [0,0,0,0,0]
b = a

print(a is b)

b[2] = 99
print(a, b)

a = [0,0,0,0,0]
b = a.copy()
print(b)
print(a is b)
print(a == b)
b[2] = 99
print(a, b)

#for 반복문으로 요소 출력하기
a = [38,21,53,62,19]
for i, v in enumerate(a, start=1) :
    print(i, v)

#가장 작은 수롸 가장 큰 수 구하기
a = [38,21,53,62,19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)

a = [38,21,53,62,19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)

a = [38,21,53,62,19]
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])

a = [10,10,10,10,10]
x = 0
for i in a :
    x += i
print(x)
print(sum(a))
