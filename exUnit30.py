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
