import math

def sieve_of_eratosthenes(n):
    
    integers = [1]*(n)
    integers[0] = 0
    integers[1] = 0
    
    for i, is_prime in enumerate(integers):
        if is_prime:
            yield i
            for k in range(i*i, n, i):
                integers[k] = 0
                
def pi(n):
    return int(n/math.log(n))
    