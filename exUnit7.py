#값을 여러 개 출력하기
print(1, 2, 3)
print('Hello', 'Python')

#sep로 값 사이에 문자 넣기
print(1, 2, 3, sep=', ')
print(4, 5, 6, sep=',')
print('Hello', 'Python', sep='')
print(1920, 1080, sep='x')

#줄바꿈 활용
print(1, 2, 3)
print(1, 2, 3, sep='\n')
print('1\n2\n3')

#\n: 다음 줄로 이동하며 개행이라고도 부릅니다.
#\t: 탭 문자, 키보드의 Tab 키와 같으며 여러 칸을 띄웁니다.
#\\: \ 문자 자체를 출력할 때는 \를 두 번 써야 합니다.

#end 사용하기
print(1)
print(2)
print(3)

print(1, end='')
print(2, end='')
print(3)

print(1, end=' ')    
print(2, end=' ')
print(3)
