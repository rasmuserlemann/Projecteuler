import time, math

def is_prime(x):  # Test if giving value is a prime
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True

def list_primality(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(2 * i, len(result), i):
                result[j] = False
    return result

def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def prime_factors(n):
    factors = {}
    d = 2
    while n > 1:
        while n % d == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                n = int(n)
                if d in factors:
                    factors[n] += 1
                else:
                    factors[n] = 1
            break
    return factors

def next_prime(n):
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1
    
def bruteforce(n):
    primes = list_primes(int(math.sqrt(n)))
    hybrid_integers = []
    for a in range(len(primes)):
        p = primes[a]
        for b in range(a + 1, len(primes)):
            q = primes[b]
            x = pow(p, q)*pow(q, p)
            if x <= n:
                hybrid_integers.append([x, p, q])
    return hybrid_integers
    
def primepi(limit):  # Returns an array such that array[x] = number of primes < x
    prime_gen = list_primality(limit + 50)
    primes = [x for x in range(len(prime_gen)) if prime_gen[x]]
    array = [0] * (limit + 1)
    p_index = 0
    for x in range(1, limit + 1):
        while True:
            if primes[p_index] > x:
                array[x] = p_index
                break
            p_index += 1
    return array

def C(a, b):
    # Compute in terms of log
    # q*log(p) + p*log(q) < b*log(a)
    limit = math.log(a, 10) * b
    count = 0
    p = 2
    while True:
        p_log = math.log(p, 10)
        if 2*p*p_log > limit:
            break
        
        # Perform binary search between the next prime and limit/p_log
        # to find smallest q such that q*log(p) + p*log(q) > b*log(a)
        lo = next_prime(p)
        hi = limit//p_log
        while lo < hi:
            q = (lo + hi)//2
            q_log = math.log(q, 10)
            if p*q_log + q*p_log > limit:
                hi = q
            else:
                lo = q + 1
        
        q = int(q)
        if not is_prime(q):
            q = next_prime(q)
        q_log = math.log(q, 10)
        
        if p == 2:
            pp = primepi(next_prime(q))
        
        if p*q_log + q*p_log == limit:
            count += (pp[q] - pp[p])
            
        elif p*q_log + q*p_log > limit:
            count += (pp[q] - pp[p] - 1)
            
        elif p*q_log + q*p_log < limit:
            q = next_prime(q)
            count += (pp[q] - pp[p] - 1)
            
        p = next_prime(p)
        
    return count

if __name__ == "__main__":
  while True:
    a, b = input("Input 2 integers separated by a space: ").split()
    a, b = int(a), int(b)
    start_time = time.time()
    print(C(a, b))
    break
  print("--- %s seconds ---" % (time.time() - start_time))