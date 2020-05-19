#변수의 사용 범위 알아보기
#x = 10 #전역변수
#def foo():
#    print(x)
#
#foo()
#print(x)


#def foo():
#    x = 10 #전역변수
#    print(x)
    
#foo()
#print(x)

#x = 10
#def foo():
#    x = 20
#    print(x)
#
#foo()
#print(x)

#x = 10
#def foo():
#    global x 
#    x = 20
#    print(x)
#
#foo()
#print(x)

def foo():
    global x
    x = 20
    print(x)

foo()
print(x)

def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()
 
print_hello()

def A():
    x = 10
    def B():
        x = 20
    B()
    print(x)
A()

def A():
    x = 10
    def B():
        nonlocal x
        x = 20

    B()
    print(x)
A()

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()

x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x + 30
            print(x)
        C()
    B()
A()

#클로저 사용하기
def clac():
    a= 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add
c = clac()
print(c(1),c(2),c(3),c(4),c(5))

#클로저의 지역 변수 변경하기
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
c = calc()
c(1)
c(2)
c(3)
