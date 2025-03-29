import mathlib.factorization as factorization

def test_naive():
    
    assert factorization.naive(13195) == [5,7,13,29]
    
def test_naive_prime():

    assert factorization.naive(2179) == [2179]
    
def test_exponents():
    
    assert [(2, 3), (3, 2), (7, 1)] == factorization.complete(2**3 * 3**2 * 7)
    
def test_2():
    assert factorization.naive(2) == [2]
    
def test_1():
    assert factorization.naive(1) == []
    
def test_8():
    assert factorization.naive(8) == [2]
    
def test_sigma_28_0():
    assert factorization.sigma(12, 0) == 6
    
def test_sigma_12_1():
    assert factorization.sigma(12, 1) == 28