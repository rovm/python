#else 사용하기
#if 조건식:
#     코드1
#else:
#     코드2

#else 들여쓰기
x = 10
if x == 10:
    print('10입니다.') 
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')

#if 조건문의 동작 방식 알아보기
if True:
    print('참')    
else:
    print('거짓')
 
if False:
    print('참')
else:
    print('거짓')   
 
if None:
    print('참')
else:
    print('거짓') #None은 거짓

#if조건문에 숫자 지정하기
if 0:
    print('참')
else:
    print('거짓') #0은 거짓
 
if 1:
    print('참') #1은 참
else:
    print('거짓')
 
if 0x1F: #16진수
    print('참') #0x1F는 참
else:
    print('거짓')
 
if 0b1000: #2진수
    print('참') #0b1000은 참
else:
    print('거짓')
 
if 13.5: #실수
    print('참') #13.5는 참
else:
    print('거짓')
    
#if조건문에 문자열 지정하기
if 'Hello': #문자열
    print('참') #문자열은 참
else:
    print('거짓')
 
if '': #빈 문자열
    print('참')
else:
    print('거짓') #빈 문자열은 거짓

#조건식을 여러 개 지정하기
x = 10
y = 20
 
if x == 10 and y == 20: #x가 10이면서 y가 20일 때
    print('참')
else:
    print('거짓')
