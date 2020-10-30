lim = 8000
lim2 = 100000

def primes(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes
P = primes(lim)
P2 = primes(lim2)
sums = []
prod = []
for x1 in P:
    print(x1)
    for x2 in [x for x in P if x < x1]:
        for x3 in [x for x in P if x < min(x2, x1)]:
            for x4 in [x for x in P if x < min(x1,x2,x3)]:
                for x5 in [x for x in P if x < min(x1,x2,x3,x4)]:
                    conc1 = int(str(x1) + str(x2))
                    conc2 = int(str(x2) + str(x1))
                    conc3 = int(str(x2) + str(x3))
                    conc4 = int(str(x3) + str(x2))
                    conc5 = int(str(x3) + str(x4))
                    conc6 = int(str(x4) + str(x3))
                    conc7 = int(str(x4) + str(x5))
                    conc8 = int(str(x5) + str(x4))
                    conc9 = int(str(x1) + str(x3))
                    conc10 = int(str(x3) + str(x1))
                    conc11 = int(str(x1) + str(x4))
                    conc12 = int(str(x4) + str(x1))
                    conc13 = int(str(x1) + str(x5))
                    conc14 = int(str(x5) + str(x1))
                    conc15 = int(str(x2) + str(x4))
                    conc16 = int(str(x4) + str(x2))
                    conc17 = int(str(x2) + str(x5))
                    conc18 = int(str(x5) + str(x2))
                    conc19 = int(str(x3) + str(x5))
                    conc20 = int(str(x5) + str(x3))
                    if set([conc1,conc2,conc3,conc4,conc5,conc6,conc7,conc8,conc9,conc10,conc11,conc12,conc13,conc14,conc15,conc16,conc17,conc18,conc19,conc20]).issubset(P2):
                        sums.append(sum([conc1,conc2,conc3,conc4,conc5,conc6,conc7,conc8,conc9,conc10,conc11,conc12,conc13,conc14,conc15,conc16,conc17,conc18,conc19,conc20]))
                        
print(min(sums))
                    
        

