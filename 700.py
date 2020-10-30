lim = 10000000000
min = 4503599627370517
total = 0

for k in range(1,lim):
    num = 1504170715041707*k % 4503599627370517
    if num < min:
        min = num
        total += num

print(total)