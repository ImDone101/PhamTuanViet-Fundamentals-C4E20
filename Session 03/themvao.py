fav = ["Reading", "Gaming", "Translating"]
print("Here are your favorite things", sep=', ')
print(*fav)
new_fav = input("Thich gi nua: ")
fav.append(new_fav)
print("New list", sep=', ')
print(*fav)

