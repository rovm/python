#함수 만들기
def hello():
    print('Hello, world!')

hello()

#함수 작성과 호출 순서
#hello()
#def hello():
#print('Hello, world!')
#Error 발생 함수 생성전에 호출 불가

#덧셈 함수 만들기
def add(a,b):
    print(a+b)

add(10,20)

def add(a,b):
    """a 와 b를 더한후 값을 반환하는 함수"""
    return a + b

x = add(10,20)
print(x)
print(add.__doc__)
print(help(add))

#함수 결과를 반환하기
def add(a,b):
    return a+b

print(add(10,20))

#return 으로 함수 중간에서 빠져나오기
def not_ten(a):
    if a == 10:
        return
    print(a, '입니다.',sep="")
not_ten(5)
not_ten(10)

#함수에서 값을 여러 개 반환하기
def add_sub(a,b):
    return a+b, a-b
x,y = add_sub(10,20)
print(x, y)

#함수의 호출 과정 알아보기
def mul(a, b):
    c = a * b
    return c
 
def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)
 
x = 10
y = 20
add(x, y)
