from random import randint
mood_point = randint(0, 100)

print("Hi there! My name is Mr Tam trang")
if mood_point < 30:
    print("Hoi sad 1 chut")
elif mood_point < 60:
    print("Cung binh thuong thoi")
else:
    print("Vui")