import math
from operator import mul
from functools import reduce

def prime_factors(n):
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

def totient(n):
    if n == 1: return 1
    return int(round(n * reduce(mul, [1 - 1.0 / p for p in prime_factors(n)])))

M = 100
top = 10**7
for d in range(2,top):
    dig1 = [int(x) for x in str(d)]
    tot = totient(d)
    dig2 = [int(x) for x in str(tot)]
    if sorted(dig1)==sorted(dig2) and d/tot<M:
        print(d)
        M = d/tot
        