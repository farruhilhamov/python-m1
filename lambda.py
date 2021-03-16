#!/usr/bin/env/ python3

from functools import *

def main():
    l = [1,2,3,4,5]
    l2 = [6,7,8,9,10]
    inc = lambda c:c+1
    s = list(map(lambda x,y:x + y ,l,l2)) 
    print(s)
    '''     x = 0 ,он обновляеться и добавляет ,y ,y = каждый элем в l  '''
    s = reduce(lambda x,y:x+y,l)
    print(s)
if __name__ == "__main__":
    main()