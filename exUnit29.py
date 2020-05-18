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
