#람다 표현식으로 함수 만들기
def plus_ten(x):
    return x + 10

print(plus_ten(1))

#람다 표현식을 인수로 사용하기
def plus_ten(x):
    return x +10

print(list(map(plus_ten,[1,2,3])))

#람다 표현식에 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))

#map에 객체를 여러 개 넣기
a = [1,2,3,4,5]
b = [2,4,6,8,10]
print(list(map(lambda x, y: x * y, a, b)))

#filter 사용하기
def f(x):
    return x > 5 and x <10
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f, a)))

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(lambda x: x > 5 and x < 10, a)))

a = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(lambda x,y : x + y, a))
