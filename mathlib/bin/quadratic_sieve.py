import argparse

from mathlib.quadratic_sieve.quadratic_sieve import quadratic_sieve

parser = argparse.ArgumentParser(prog="Quadratic Sieve", description="Factors a number")

parser.add_argument("n", metavar="int", type=int, help="number to be factored")
parser.add_argument("-b", "--smoothness-bound", required=False, default=20, metavar="int", type=int, help="smoothness bound")
parser.add_argument("-i", "--sieve-bound", required=False, default=20, metavar="int", type=int, help="sieve interval bound")
parser.add_argument("-p", "--num-processes", required=False, default=0, metavar="int", type=int, help="number of processes used to factor n")

def main(args):
    print(quadratic_sieve(**vars(args)))
    
if __name__ == "__main__":
    
    main(parser.parse_args())