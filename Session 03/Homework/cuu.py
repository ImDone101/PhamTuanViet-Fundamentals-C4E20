sheeps = [5, 7, 300, 90, 24, 50, 75]
to_nhat = 0
tong = 0
n = int(input("Nhap so thang: "))
print("Xin chao, toi la Viet va day la dan cuu cua toi: ")
print(sheeps)
for s in sheeps:
    if s > to_nhat:
        to_nhat = s
print("Con cuu to nhat cua toi co size", to_nhat, "Xen long no thoi")

sheeps[sheeps.index(to_nhat)] = 8
print("Sau khi xen long, dan cuu cua toi con: ")
print(sheeps)
for thang in range(1, n + 1):
    to_nhat = 0
    print("THANG", thang, ':')
    for index, size in enumerate(sheeps):
        sheeps[index] = size + 50
    print("1 thang da qua, cuu cua toi day: ")
    print(sheeps)
    for s in sheeps:
        if s > to_nhat:
            to_nhat = s
    if thang < n:
        print("Con cuu to nhat cua toi co size", to_nhat, "Xen long no thoi")
        sheeps[sheeps.index(to_nhat)] = 8
        print("Sau khi xen long, dan cuu cua toi con: ")
        print(sheeps)
        print()

for so_luong in sheeps:
    tong += so_luong
print("Tong the dan cuu co size: ", tong)
print("Toi se kiem duoc {} * 2$ = {}".format(tong, tong*2))