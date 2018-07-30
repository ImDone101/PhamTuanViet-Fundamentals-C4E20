n = int(input("Nhap so muon tim hieu: "))
count = 0
check = True
if n == 1:
    print("So nguyen to")
    check = False
while check:
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("So nguyen to")
        check = False
    else:
        print("Khong phai")
        check = False

    