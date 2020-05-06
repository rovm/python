#문자열 사용하기
hello = 'Hello, world!'
print(hello)

hello = "Hello, world!"
print(hello)

hello = '''Hello, Python!'''
print(hello)

python = """Python Programming!"""
print(python)

hello = '''Hello, world!
안녕하세요.
Python입니다.'''
print(hello)

#문자열 안에 작은따옴표나 큰따옴표 포함하기
s = "Python isn't difficult"
print(s)

s = 'He said "Python is easy"'
print(s)

#s = 'Python isn't difficult'
#SyntaxError: invalid syntax
#s = "He said "Python is easy""
#SyntaxError: invalid syntax

single_quote = '''"안녕하세요."
'파이썬'입니다.'''
 
double_quote1 = """"Hello"
'Python'"""
 
double_quote2 = """Hello, 'Python'"""    # 한 줄로 작성
 
print(single_quote)
print(double_quote1)
print(double_quote2)
