#!/usr/bin/env/ python3


class yasherica(object):
    def polzat():
        print("ya polzayu")
    def __init__(self):
        yasherica.polzac = True


class ptica(object):
    def letat():
        print("ya lechu")
    def __init__(self):
        ptica.letat = True

class Hybrid(yasherica,ptica):
    def __init__(self):
        y = yasherica
        p = ptica
        y.polzat()
        p.letat()    

    

def main():
    pterodactel = Hybrid()
    
if __name__ == "__main__":
    main()