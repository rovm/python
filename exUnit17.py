#while 반복문 출력
i = 1                   
while i <= 10:         
     print('Hello, world! ', i)   
     i += 1                 

i = 10                   
while i > 0:         
     print('Hello, world! ', i)   
     i -= 1            

import random

i = 0
while i != 3:
    i = random.randint(1,6)
    print(i)

dice = [1, 2, 3, 4, 5, 6]
print('random => ', random.choice(dice))

#while 반복문으로 무한 루프

#while True:
#   print('무한 루프')

#while 1:
#   print('무한 루프')

#while 'Hello':
#   print('무한 루프')
