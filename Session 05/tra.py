teen = {
    "hc" : "hoc",
    "ng" : "nguoi",
    "lm" : "lam",
    "r" : "roi",
    "ck" : "chong",
    "vk" : "vo"
}
bai = True
while bai:
    print("*" * 20)
    for key in teen.keys():
        print(key, end = "\t")
    print()
    print("*" * 20)

    n = input("Muon dich cai nao: ")
    print("*" * 20)
    if n in teen:
        print("Da dich ra: ", teen[n])
    else:
        choice = input("Khong co, ban muon cap nhat khong ? ")
        if choice == "Y":
            new = input("Ban dich the nao: ")
            teen[n] = new
            print("Da cap nhat")
        elif choice == "N":
            print("ket thuc")
            bai = False

    print("*" * 20)

