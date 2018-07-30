print("Chao mung den he thong")
userName = 'VietPham'
passWord = '123456'
count = 3

while count > 0:
    u = input("Username: ")
    if u == userName:
        p = input("Password: ")
        if p != passWord:
            print("Password sai")
            count -= 1
        else:
            print("Dang nhap thanh cong")
            break
    else:
        print("Username sai")
print("Khoa may")
