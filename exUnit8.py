#불과 비교 연산자 사용
print(True) # True
print(False) # False

#비교 연산자의 판단 결과
print(3>1) # True

#숫자가 같은지 다른지 비교하기
print(10 == 10) # True
print(10 != 5) # True

#문자열이 같은지 다른지 비교하기
print('Python' == 'Python') # True
print('Python' == 'python') # False
print('Python' != 'python') # True

#부등호 사용하기
print(10 > 20) # False
print(10 < 20) # True
print(10 >= 20) # False
print(10 <= 20) # True

#객체가 같은지 다른지 비교하기
print(1 == 1.0) # True
print(1 is 1.0) # False
print(1 is not 1.0) # True
#id 값을 사용하여 비교
print(id(1)) # 1673918384
print(id(1.0)) # 49393632

#논리 연산자 사용하기
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
print(not True) # False
print(not False) # True
print(10 == 10 and 10 != 5) # True
print(10 > 5 or 10 < 3) # True
print(not 10 > 5) # False
print(not 1 is 1.0) # True

#bool 값
print(bool(1)) # True
print(bool(0)) # False
print(bool('Aaaa')) # True
# 0, 0.0이외의 모든 것은 True

