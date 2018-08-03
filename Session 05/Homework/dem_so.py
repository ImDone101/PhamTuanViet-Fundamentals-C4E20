numbers = [1, 6, 7, 3, 4, 2, 1, 4, 3, 1]
n = int(input("Nhap 1 so: "))
dem = 0

for i in numbers:
    if i == n:
        dem += 1
print("{} xuat hien {} lan trong list".format(n, dem))