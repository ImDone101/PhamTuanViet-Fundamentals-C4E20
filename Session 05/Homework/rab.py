tho = {0 : 1, 1 : 2}

for i in range (3):
    tho[i + 2] = tho[i] + tho[i + 1]
for key, value in tho.items():
    print('Thang {}: {} cap tho'.format(key, value))
    # print(tho)