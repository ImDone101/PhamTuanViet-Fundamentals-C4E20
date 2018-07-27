from turtle import *

speed(1)
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
c_i = 0

for hinh in range(5):
    canh = 4
    color(colors[c_i])
    begin_fill()
    while canh > 0:
        canh -= 1
        if canh % 2 ==1:
            forward(50)
            left(90)
        else:
            forward(80)
            left(90)
    end_fill()
    forward(50)
    c_i += 1

mainloop()