from mathlib.tonelli_shanks import _powers_of_2, find_root_mod_p

def test_powers_of_2_2():
    assert _powers_of_2(2) == (1, 1)
    
def test_powers_of_2_3():
    assert _powers_of_2(3) == (0, 3)   

def test_powers_of_2_4():
    assert _powers_of_2(4) == (2, 1)

def test_powers_of_2_6():
    assert _powers_of_2(6) == (1, 3)
    
def test_find_root_mod_p_5_41_with_z():
    assert find_root_mod_p(5, 41, z=3) == 28
    
def test_find_root_mod_p_5_41():
    assert find_root_mod_p(5, 41) == 28
    
def test_find_root_mod_p_9_41():
    assert find_root_mod_p(9, 41) == 3