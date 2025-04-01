import multiprocessing as mp

def get_parallel_runner(p):

    if p == 0:
        p = None
    
    def _parallel_runner(f, iterable):
        with mp.Pool(p) as pool:
            return pool.map(f, iterable)
        
    return _parallel_runner