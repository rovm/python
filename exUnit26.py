#세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)

fruits = {'orange', 'orange', 'cherry'}
print(fruits)

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('orange' in fruits)
print('peach' in fruits)
print('orange' not in fruits)
print('peach' not  in fruits)

#set를 사용하여 세트 만들기
a = set('apple')
print(a)

b = set(range(5))
print(b)

c = set()
print(c)

#집합연산 사용하기
a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)
print(set.union(a,b))
print(a&b)
print(set.intersection(a,b))
print(a-b)
print(set.difference(a,b))
print(a^b)
print(set.symmetric_difference(a,b))

#집합 연산 후 할당 연산자 사용하기
a = {1,2,3,4}
a |= {5}
a.update({6})
print(a)

a = {1,2,3,4}
a &= {0,1,2,3,4}
print(a)
a = {1,2,3,4}
a.intersection_update({0,1,2,3,4})
print(a)

a = {1,2,3,4}
a -= {3}
print(a)
a = {1,2,3,4}
a.difference_update({3})
print(a)

a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)
a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})
print(a)

#부분 집합과 상위집합 확인하기
a = {1,2,3,4}
print(a <= {1,2,3,4})
print(a.issubset({1, 2, 3, 4, 5}))
print(a < {1, 2, 3, 4, 5})
print(a >= {1, 2, 3, 4})
print(a.issuperset({1, 2, 3, 4}))
print(a>{1,2,3})

#세트가 같은지 다른지 확인하기
a = {1,2,3,4}
print(a == {1,2,3,4})
print(a == {4,3,2,1})
print(a != {1,2,3,4})

#세트가 겹치지 않는지 확인하기
a = {1,2,3,4}
print(a.isdisjoint({5,6,7,8}))
print(a.isdisjoint({3,4,5,6}))

#세트에 요소 추가하기
a = {1,2,3,4}
a.add(5)
print(a)
a.remove(3)
print(a)
a.discard(2)
print(a)
a.discard(3)
print(a)

#세트에서 임의의 요소 삭제하기
a = {1,2,3,4}
a.pop()
print(a)

#세트의 모든 요소를 삭제하기
a.clear()
print(a)

#세트의 요소 개수 구하기
a = {1,2,3,4}
print(len(a))
