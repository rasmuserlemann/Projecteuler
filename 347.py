lim = 10000000

import numpy
def primes(n):
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
      
P = list(primes(int(lim/2)))

N = []
for p in P:
    for q in [x for x in P if x > p]:
        if p*q>lim:
            break
        M = []
        for k1 in range(1,25):
            if p**(k1)*q>lim:
                break
            for k2 in range(1,25):
                if p**(k1)*q**(k2)>lim:
                    break
                M.append(p**(k1)*q**(k2))
        N.append(max(M))

print(sum(N))
    
    