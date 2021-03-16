#!/usr/bin/env/ python3
import random
def main():
    a = ["a","e","i","o","u","y"]
    b = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","w","x","z"]
    nick = ''
    myrange = int(input("enter lenght of your nickname: "))
    r = 20

    for i in range(r):

        c = chr(random.randrange(97,121))
        ranglas = []
        ransogl = []
        
    
        for i in range(myrange//2):
            
            if myrange % 2 != 0:
                if random.randint(1,2)% 2 == 0:
                    nick += (a [random.randint(1, len(a)-1)])
                else:
                    nick += (a [random.randint(1, len(a)-1)])

            ransogl = (b [random.randint(1, len(b)-1)])
            ranglas = (a [random.randint(1, len(a)-1)])
            nick += ransogl + ranglas

        '''декоратор'''
        def decorator(nick):
            dec = chr(random.randint(9400,11197))
            d = (dec + nick + dec)
            print(d)

        decorator(nick)
        nick = ''


if __name__ == "__main__":
    main()