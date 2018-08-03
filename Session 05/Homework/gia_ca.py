gia_ca = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

co_phieu = {
    'banana' : 6,
    'apple' : 0,
    'orange' : 32,
    'pear' : 15
}

tong = 0

for key in gia_ca:
    print(key, 'gia : ' + str(gia_ca[key]), 'co_phieu : ' + str(co_phieu[key]), sep = '\n', end = '\n\n')
    value = gia_ca[key] * co_phieu[key]
    tong += value

print('Tong gia tri la: ',tong)