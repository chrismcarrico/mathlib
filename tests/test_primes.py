import lib.primes as primes

def test_first_10_primes():
    sieve = primes.sieve_of_eratosthenes(100)
    
    first_10 = [2,3,5,7,11,13,17,19,23,29]
    
    assert first_10 == [next(sieve) for _ in range(10)]
    
