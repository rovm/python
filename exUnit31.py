#재귀호출 사용하
def hello(count):
    if count == 0:
        return

    print('Hello, Wolrd!', count)

    count -= 1
    hello(count)

hello(5)

#재귀함수로 팩토리얼 구하기
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
