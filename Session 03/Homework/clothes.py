quanao = ["T-Shirt", "Sweater"]
bt = True

while bt:
    option = input("Chao mung den voi cua hang, ban muon lam gi (C, R, U, D) ? ")
    if option == 'C' or option == 'c':
        new_qa = input("Them gi vao: ")
        quanao.append(new_qa)
        print("Quan ao: ", sep = ', ')
        print(*quanao)
    if option == 'R' or option == 'r':
        print("Quan ao: ", sep = ', ')
        print(*quanao)
    if option == 'U' or option == 'u':
        upd_vtri = int(input("Cap nhat vi tri ?: "))
        while upd_vtri - 1 > len(quanao) or upd_vtri - 1 < 0:
            print("Xin moi nhap lai")
            upd_vtri = int(input("Cap nhat vi tri ?: "))
        new = input("Mon hang moi la: ")
        quanao[upd_vtri - 1] = new
        print("Quan ao: ", sep = ', ')
        print(*quanao)
    if option == 'D' or option == 'd':
        del_vtri = int(input("Xoa cho nao: "))
        while del_vtri -1 > len(quanao) or del_vtri - 1 < 0:
            print("Xin moi nhap lai")
            del_vtri = int(input("Xoa cho nao: "))
        del quanao[del_vtri - 1]
        print("Quan ao: ", sep = ', ')
        print(*quanao)