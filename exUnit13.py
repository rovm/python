#if 조건문으로 특정 조건일 때 코드 실행하기

#if 조건식:
#     코드

x = 10
if x == 10:
    pass #pass 는 아무것도 하지 않고 넘긴다

#if 조건문과 들여쓰기
x = 10
 
if x == 10:
     print('x에 들어있는 숫자는')
     print('10입니다.')

#중첩 if 조건문 사용하기
x = 15
 
if x >= 10:
     print('10 이상입니다.')
 
     if x == 15:
         print('15입니다.')
 
     if x == 20:
         print('20입니다.')

x = int(input())         
if x == 10:               
    print('10입니다.')    
if x == 20:              
    print('20입니다.')   
