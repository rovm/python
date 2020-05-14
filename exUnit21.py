#사각형 그리기

import turtle as t

t.shape('turtle')

#t.forward(100)
#t.right(90)
#t.forward(100)
#t.right(90)
#t.forward(100)
#t.right(90)
#t.forward(100)

#for i in range(4):    
#    t.forward(100)
#    t.right(90)

#t.color('#FF69B4')
#t.begin_fill()
#for i in range(5):
#    t.fd(100)
#    t.rt(360/5)
#t.end_fill()

#t.circle(120)

t.speed('fastest')
#for i in range(60):
#    t.circle(120)
#    t.right(360 /60)

#for i in range(300):
#    t.fd(i)
#    t.rt(91)

for i in range(100):
    for j in range(4):
        t.fd(100)
        t.rt(90)
    t.rt(91)

t.mainloop()
