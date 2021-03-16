
mysymb = input("enter symb: ")

for i in range(30000):
    if chr(i) == mysymb:
        print('symbol' + chr(i) + " is "+ str(i))

#for i in range(9472,11167):
#    print(chr(i)+chr(i+1)+chr(i-1))
while True:
    for i in range(11164,11168):
        if i != 11167:
            for z in range(10): 
                chrome = (chr(i)+"WoW"+chr(i))
                word = "\n"
                
                print(word*15 +" "*5 + chrome)