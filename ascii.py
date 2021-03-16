#!/usr/bin/env/ python3
import random
def main():
    n = ''
    for i in range(30000):
        #n += chr(random.randint(1,2000))
        if len(n) != 50: 
            n += chr(i)
        else:
            print(n)
            n = ""
    #print(n)
if __name__ == "__main__":
    main()