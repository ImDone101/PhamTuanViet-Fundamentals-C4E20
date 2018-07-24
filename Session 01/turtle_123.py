from turtle import *
n = int(input("Nhap so n: "))
shape("turtle")
color("green")


for i in range(n):
  left(360/n)
  forward(100)


mainloop()