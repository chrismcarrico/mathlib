import lib.triangular_numbers as triangular_numbers

def test_nth_triangular_number_7():
    assert triangular_numbers.nth_triangular_number(7) == 28
    
def test_generator_7():
    
    generator = triangular_numbers.generator()
    
    while True:
        a,b = next(generator)
        
        if a == 7:
            break
        
    assert b == 28