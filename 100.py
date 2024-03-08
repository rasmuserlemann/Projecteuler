import math
import numpy
from operator import mul
from functools import reduce


def primes(n):
    res = set()
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.add(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.add(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.add(n)
    return res

rad = []
top = 100000
for ind in range(1,top+1):
    rad.append(numpy.product(list(primes(ind))))

N = 10000
rad2 = sorted(rad)
num = rad2[N-1]
for k in range(len(rad)):
    if rad[k]==num:
        print(k+1)