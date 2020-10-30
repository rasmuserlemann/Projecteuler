from math import sqrt; from itertools import count, islice

def prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def diag(n):
    return((2*n+1)**2)
def diag1(n):
    return((2*n+1)**2-2*n)
def diag2(n):
    return((2*n+1)**2-4*n)
def diag3(n):
    return((2*n+1)**2-6*n)

d1 = []
d2 = []
d3 = []
d4 = []
for k in range(0,100000):
    d1.append(diag(k))
    d2.append(diag1(k))
    d3.append(diag2(k))
    d4.append(diag3(k))

sum = 0

for k in range(1,100000):
    if prime(d1[k]):
        sum = sum + 1
    if prime(d2[k]):
        sum = sum + 1
    if prime(d3[k]):
        sum = sum + 1
    if prime(d4[k]):
        sum = sum + 1
    if sum/(4*k+1) < 0.1:
        print(k)