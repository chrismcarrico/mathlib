import math
import functools

import mathlib.primes as primes
import mathlib.legendre as legendre
import mathlib.tonelli_shanks as tonelli_shanks
import mathlib.parallel_runner as parallel_runner

def _find_roots(p):
    s1 = tonelli_shanks.find_root_mod_p(0, p)
    s2 = (p-s2)%p
    
def _get_exponent_vector(x, n, sqrt_n, factor_base):
    
    q = pow(x + sqrt_n, 2) - n
    vector: list[int] = [0]*len(factor_base)
    
    for i, p in enumerate(factor_base):
        
        e = 0
        
        while q % p == 0:
            e += 1
            q //= p
        
        vector[i] = e % 2
        
    if not q == 1:
        return None
        
    return (x, vector)    
        

def _sieve(n, factor_base, runner, sieve_interval):
    sqrt_n = math.floor(math.sqrt(n))
    get_exponent_vector = functools.partial(_get_exponent_vector, n=n, sqrt_n=sqrt_n, factor_base=factor_base)
    
    vectors = runner(get_exponent_vector, range(-sieve_interval, sieve_interval+1))
    vectors = [i for i in vectors if i is not None]
    
    return vectors


def quadratic_sieve(n: int, smoothness_bound:int, num_processes: int, sieve_bound: int) -> tuple:
    
    factor_base = [p for p in primes.sieve_of_eratosthenes(smoothness_bound) if legendre.legendre_symbol(n, p) == 1]
    runner = parallel_runner.get_parallel_runner(num_processes)
    vectors = _sieve(n, factor_base, runner, sieve_bound)
    
    return vectors