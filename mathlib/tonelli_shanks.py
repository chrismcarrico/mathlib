import random

import mathlib.legendre as legendre

def _powers_of_2(n):
    
    assert n > 1
    
    s = 0
    n_0 = n
    while n % 2 == 0:
        n //= 2
        s += 1
    
    q = n_0//pow(2, s)
    return s, q
    

def find_root_mod_p(n: int, p: int, z = None) -> int:
    """Returns a number r such that r^2 = n mod p"""
    
    s,q = _powers_of_2(p-1)
    
    if z == None:
        while True:
            z = random.choice(range(2, p))
            residue = legendre.legendre_symbol(z, p)
            
            if residue == -1 or residue == p-1:
                break
    else:
        assert not legendre.legendre_symbol(z, p) == 1
        
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q+1)//2, p)
    
    while True:
        
        if t == 0:
            return 0
        if t == 1:
            return r
        
        t_prime = t
        i = 1
        while True:
            t_prime = pow(t_prime, 2, p)
            
            if t_prime == 1:
                break
            if i == m:
                return None
            
            i += 1
        
        b = pow(c, pow(2, m-i-1),p)
        m = i
        c = pow(b, 2, p)
        t = t*pow(b, 2) % p 
        r = r*b % p    
    
    
       