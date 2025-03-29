def nth_triangular_number(n):
    return sum(range(n+1))

def formula(n):
    return (n**2 + n) // 2
 
def generator():
    
    a, b = 1, 1
    
    while True:
        yield a
        a += 1
        b += a