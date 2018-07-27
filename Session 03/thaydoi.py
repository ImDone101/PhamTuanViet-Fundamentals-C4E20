fav = ["Reading", "Gaming", "Translating"]
print("Here are your favorite things")
for index, item in enumerate(fav):
    print("{}, {}".format(index+1, item))
n = int(input("Muon thay cho nao: "))
update_fav = input("Nhap cai moi: ")
fav[n-1] = update_fav
print("List moi day: ")
print(*fav,sep = ', ')
