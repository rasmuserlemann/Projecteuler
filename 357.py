def prim(n):
  m = n+1
  #numbers = [True for i in range(m)]
  numbers = [True] * m #EDIT: faster
  for i in range(2, int(n**0.5 + 1)):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes

P = prim(lim+5)

import math

def div(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if i + n/i not in P:
                return 0
    return(n)
            

lim = 100000000
s = 0

for k in range(1,lim+1):
    s + s + div(k)
    