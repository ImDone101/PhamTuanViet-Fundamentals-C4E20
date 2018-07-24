from turtle import*

speed(2)
shape("turtle")
color("green")

length = 5

for i in range(100):
    forward(length)
    left(90)

    length += 10

mainloop()