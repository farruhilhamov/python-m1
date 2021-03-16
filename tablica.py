#!/usr/bin/env/ python3

#comment

#def main():
#   max = 10
#   l = 1
#   tab = [[],[],[],[],[],[],[],[],[],[]]
#   s = 0
#   for i in range(10):
#       for i in range (10):
#        s += i+1 * l-1
#        sl = str(i+1) + ' * ' + str(l-1), '='  , str(s)
#        s = 0
#        tab[l-1].append(sl)
#        if i == 9:
#            l +=1
    
def main():
    l = 1
    s=""
    i = 0
    for o in range (1 ,101):
        i += 1
        if i >= 11:
           l += 1
           i = 1
        if l == 11:
        
            break
        if l == 6 and i == 1:
            print('')
            print('')
            
        s = s + str(l) + ' * ' + str(i) + ' = ' + str(l * i) + '\t'

        
               
        if ((i%5)==0):
           print(s)
           s=""


    


if __name__ == "__main__":
   main()
   