n = int(input("Nhap so n: "))
for i in range(1, n+1):
    for j in range(1,n+1):
        print('%3d' %(i * j), end = ' ')
    print()