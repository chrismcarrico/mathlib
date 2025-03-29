import lib.fibonacci_sequence as fibonacci_sequence

def test_first_10_fibonacci_sequence():
    first_10 = [1,2,3,5,8,13,21,34,55,89]
    sequence = fibonacci_sequence.generator()
    assert first_10 == [next(sequence) for _ in range(10)]