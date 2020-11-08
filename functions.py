import numpy as np
import sys

def expo(x):
    return np.exp(x)

def show_expo(n):
    for i in range(n):
        print(expo(float(i)))

def main():
    
    n = 10

    if len(sys.argv) > 1:
        n = int(sys.argv)
    # argv is the number of command line arguments
    
    print("the value of n = ", n)
    print("the value of argv = ", sys.argv)
    show_expo(n)

if __name__ == "__main__":
    main()

