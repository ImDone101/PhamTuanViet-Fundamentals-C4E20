from random import randint
dau = 0
cuoi = 100
check = True
chon =' '
print("Hay de toi doan so cua ban. Nhan Enter de tiep tuc")
input()
print("""Nhan C neu nhu correct
Nhan S neu nhu smaller
Nhan L neu nhu larger""")
while check:
    giua = (dau + cuoi) // 2
    chon = input("{} co dung khong ? ".format(giua))
    if chon == 'C':
        print("Biet ngay ma")
        break
    elif chon == 'S':
        dau = giua
    elif chon == 'L':
        cuoi = giua