#!/usr/bin/env/ python3

from functools import *

def main():
    l = [1]
    for i in range(50):
        d = list(filter(reduce(lambda x,y:x+y,l,)))
        d(i)

    print(l)
    
    
    
if __name__ == "__main__":
    main()