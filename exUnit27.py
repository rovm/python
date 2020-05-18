#파일사용하기
file = open('hello.txt', 'w')
file.write('Hello World!')
file.close()

file = open('hello.txt','r')
s = file.read()
print(s)
file.close()
