n = input("Nhap 1 cau: ").lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

demChu = {}
for char in n:
    if char in alphabet:
        if char in demChu:
            demChu[char] += 1
        else:
            demChu[char] = 1

key = demChu.keys()
for char in sorted(key):
    print(char, demChu[char])
