m = float(input("Enter your weight: "))
h = float(input("Enter your height: "))
BMI = m / (h * h)
print(BMI)

if BMI < 16:
    print("Thieu can nghiem trong")
elif 16 <= BMI <18.5:
    print("Thieu can")
elif 18.5 <= BMI < 25:
    print("Binh thuong")
elif 25 <= BMI < 30:
    print("Thua can")
else:
    print("Beo phi")