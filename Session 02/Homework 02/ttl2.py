from turtle import *

shape("turtle")

for i in range (3, 7):
    g = 360/i
    if i % 2 == 1:
        color("blue")
        for k in range(i):
            forward(100)
            left(g)
                    
    else:
        color("red")
        for l in range(i):
            forward(100)
            left(g)
        
exitonclick()
mainloop()