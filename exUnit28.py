#회문 판별하기

str = "nurses run"
str = str.replace(" ", "");

print(str == str[::-1]) #reversed

text = "Hello"
n = 5
for i in range(len(text)-(n-1)):
    print(text[i:i+n])
