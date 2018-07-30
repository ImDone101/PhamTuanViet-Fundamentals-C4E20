from random import choice

d_sach = ["champion", "dungeon", "master", "hero"]
answ = choice(d_sach)
chu_cai = list(answ)
save = []

while len(chu_cai) > 0:
    char = choice(chu_cai)
    save.append(char)
    chu_cai.remove(char)

print(*save)
n = input("Enter the word: ")
if n == answ:
    print("Dung :))")
else:
    print("Sai :((")

    