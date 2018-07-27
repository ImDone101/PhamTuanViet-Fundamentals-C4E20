#List
#Create

menu =["Com", "Ca", "Thit bo", "Ghe", "Pizza", "Ga"]
#Separator

#Update
print(*menu, sep = ', ')
menu[4] = "Tom hum"
print(*menu, sep = ', ')

#Create
# menu.append("Ghe")
# for i in range(len(menu)):
#     print(menu[i])
# for item in menu:
#     print(item)
# for index, item in enumerate(menu):
#     print("{}, {}".format(index + 1, item))