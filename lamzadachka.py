#!/usr/bin/env/ python3
from math import *
def main():
    pow = (lambda i: sin(i)) 
    data = [pow (i) for i in range(1, 10)]
    print(data)
if __name__ == "__main__":
    main()