
for h in range(6):
    for c in range(6):
        if c <= 6 - h - 1:
            print(" ", end = "")
        else:
            print("*", end = "")
    print()