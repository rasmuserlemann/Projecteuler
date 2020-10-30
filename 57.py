max = 0
         
def sieve(n):
    primes = []
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return primes