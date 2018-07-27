from random import randint
numb = randint(1, 100)
print(numb)

play = True
count = 0

while play:
    gs = int(input("Doan so tu 1-100: "))
    if  gs > numb:
        print("Hoi to 1 chut  :(")
    elif gs < numb:
        print("Hoi be 1 chut  :(")
    else:
        print("Dung roi  :)")
        break
    count += 1
    if count == 7:
        print("Thua")
        break