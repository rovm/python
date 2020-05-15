#문자열 바꾸기
print('Hello World!'.replace('World','Python'))

#문자 바꾸기
table = str.maketrans('aeiou','12345')
print('apple'.translate(table))

#문자열 분리하기
print('apple pear grape pineapple orange'.split())

#구분자 문자열과 문자열 리스트 연결하기
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

#소문자를 대문자로 바꾸기
print('python'.upper())

#대문자를 소문자로 바꾸기
print('PYTHON'.lower())

#공백 삭제하기
print('   Python   '.lstrip())
print('   Python   '.rstrip())
print('   Python   '.strip())

#특정 문자 삭제하기
print(', Python.'.lstrip(',.'))
print(', Python.'.rstrip(',.'))
print(', Python.'.strip(',.'))

#문자열 정렬하기
print('python'.ljust(10))
print('python'.rjust(10))
print('python'.center(10))

#메서드 체이닝
print('pythoon'.rjust(10).upper())

#문자열 왼쪽에 0 채우기
print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))

#문자열 위치 찾기
print('apple pineapple'.find('pl'))
print('apple pineapple'.find('xy'))

print('apple pineapple'.rfind('pl'))
print('apple pineapple'.rfind('xy'))

print('apple pineapple'.index('pl'))
print('apple pineapple'.rindex('pl'))

#문자열 개수 세기
print('apple pineapple'.count('pl'))

#서식 지정자로 문자열 넣기
print('I am %s.' % 'james')

name = 'maria'
print('I am %s.' % name)

#서식 지정자로 숫자 넣기
print('I am %d years old.' % 20)

#서식 지정자로 소수점 표현하기
print('%f' % 2.3)
print('%.2f' % 2.3)
print('%10s' % 'python') #기본 오른쪽 정렬
print('%-10s' % 'python') #기본 왼쪽 정렬

#서식 지정자로 문자열 안에 값 여러 개 넣기
print('Today is %d %s.' % (3, 'Aprill'))

#format 매서드 사용하기
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))
print('{0} {0} {1} {1}'.format('Python', 'Script'))
print('Hello, {} {} {}'.format('Python', 'Script', 3.6))
print('Hello, {language} {version}'.format(language='Python', version=3.6))

language = 'Python'
version = 3.6
print(f'Hello, {language} {version}')
print('{{ {0} }}'.format('Python'))

#format 매서드로 무자열 정렬하기
print('{0:<10}'.format('python'))
print('{0:>10}'.format('python'))

#숫자 개수 맞추기
print('%03d' % 1)
print('{0:03d}'.format(35))

print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37 ))

print('{0:0<10}'.format(15))
print('{0:0>10}'.format(15))

print('{0:x>10}'.format(15))
print(format(1904502,','))
