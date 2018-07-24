from turtle import *
n = int(input("Nhap so hinh tron: "))
shape("turtle")
color("green")

for i in range(n):
    circle(100)
    left(60)

mainloop()