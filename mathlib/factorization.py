import math

import mathlib.primes as primes

def naive(n):
    
    prime_factors = []
    
    if n < 2:
        return []
    
    sieve = primes.sieve_of_eratosthenes(n)
    
    p = 1
    while p < math.floor(math.sqrt(n)):
        try:
            p = next(sieve)
            if n % p == 0:
                prime_factors.append(p)
        except StopIteration:
            break
        
    if prime_factors:
        return prime_factors
        
    return [n]

def sigma(n, z=0):
    
    s = 0
    i = 1
    greatest_factor = n
    
    while i < greatest_factor:
        if n%i ==0:
            s += pow(i, z)
            s += pow(n//i, z)
            greatest_factor = n//i
        i += 1
    
    return s
    
def complete(n):
    
    prime_factors = naive(n)
    
    exponents: list[tuple[int, int]] = []
    
    for i in prime_factors:
        
        e = 0
        n_remainder = n
        while n_remainder > 1 and n_remainder % i == 0:
            e += 1
            n_remainder //= i
        
        exponents.append((i, e))
        
    return exponents    
    
        