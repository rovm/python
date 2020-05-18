#위치 인수와 리스트 언패킹 사용하기
print(10, 20, 30)

#위치 인수를 사용하는 함수를 만들고 호출하기
def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)

print_numbers(10,20,30)

#언패킹 사용하기
x = [10,20,30]
print_numbers(*x)
print_numbers(*[10,20,30])

#가변 인수 함수 만들기
def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10)
print_numbers(10,20,30,40)

def print_numbers(a, *args):
    print(a)
    print(*args)

print_numbers(1)
print_numbers(1,10,20)
print_numbers(*[10,20,30])

#키워드 인수 사용하기
def personal_info(name,age,address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info('홍길동', 30, '서울시 용산구 이촌동')
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')

#키워드 인수와 딕셔너리 언패킹 사용하기
def personal_info(name,age,address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address':'서울시 용산구 이촌동'}
personal_info(**x)

#키워드 인수를 사용하는 가변 인수 함수 만들기
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
personal_info(name='홍길동')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')

y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**y)

y = {'name': '홍길동', 'address': '서울시 용산구 이촌동'}
def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

personal_info(**y)

def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1,2,3,sep=':',end='')
