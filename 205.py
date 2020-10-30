from functools import reduce
import numpy

def div(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))-{n}

def amic(n, x, t):
    if t==10000:
        return([0,0])
    divisors = div(n)
    S = numpy.sum(list(divisors))
    if S > 1000000:
        return([0,0])
    if S in x:
        return([x,t])
    new = x
    new.append(S)
    return(amic(S, new, t+1))

best = 0
for v in range(100,1000000):
    A = amic(v,[],0)
    if A[1]>best:
        best = A[1]
        print(A[0])
        
        
def pe95(L = 1000000):
    d = [1] * L
    for i in range(2, L//2):
        for j in range(2*i, L, i):
            d[j] += i

    max_cl = 0
    for i in range(2, L):
        n, chain = i, []
        while d[n] < L:
            d[n], n = L+1, d[n]
            try: k = chain.index(n)
            except ValueError: chain.append(n)
            else: 
                if len(chain[k:]) > max_cl:
                    max_cl, min_link = len(chain[k:]), min(chain[k:])
    return min_link