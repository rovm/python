#파일사용하기
file = open('hello.txt', 'w')
file.write('Hello World!')
file.close()

file = open('hello.txt','r')
s = file.read()
print(s)
file.close()

#반복문으로 문자열 여러 줄을 파일에 쓰기
with open('hello.txt','w') as file:
    for i in range(3):
        file.write('Hello, world! {}\n'.format(i))

#리스트에 들어잇는 무자열을 파일에 쓰기
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n'] 
with open('hello.txt', 'w') as file:
    file.writelines(lines)

#파일의 내용을 한 줄씩 리스트로 가져오
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

#파일의 내용을 한줄씩 읽기
with open('hello.txt','r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

#파이썬 객체를 파일에 저장하기
import pickle
 
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
 
with open('james.p', 'wb') as file:    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

#파일에서 파이썬 객체 읽기
import pickle
 
with open('james.p', 'rb') as file:    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
