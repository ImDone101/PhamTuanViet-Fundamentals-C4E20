from turtle import *

speed(1)
shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
c_i = 0

for canh in range(3, 8):
    color(colors[c_i])
    forward(100)
    for i in range(canh - 1):
        lt(360/canh)
        forward(100)
    left(360 / canh)
    c_i += 1

mainloop()

