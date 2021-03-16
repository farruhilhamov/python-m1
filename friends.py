#!/usr/bin/env/ python3
def main():
    while True:
        
        #names = input("Enter your friends: ")
        #if names == "":
        #    break
        #names = names.strip()
        #lnames = names.split()
        #while (names.find("  ")>=0):
        #    names = names.replace("  "," ")
        #print(names)
        #print(lnames)
        var = input("a/r/w/q: ")
        '''varianti'''


        '''read mode'''
        if var == 'r':
            with open("friends.txt","r") as file:
                content = file.readlines()
                for elem in content:
                    print(elem,end="")
            
            '''write mode'''

        elif var == 'w':
            names = input("Enter your friends: ")
            if names == "":
                break
            names = names.strip()
            lnames = names.split()
            while (names.find("  ")>=0):
                names = names.replace("  "," ")
        
            with open("friends.txt","w") as file:
                for name in lnames :
                    print(name, file = file)
                    #file.write(name + "\n")
            with open("friends.txt","r") as file:
                content = file.readlines()
                for elem in content:
                    print(elem,end="")

        
        elif var == "w":
            names = input("Enter your friends: ")
            if names == "":
                break
            names = names.strip()
            lnames = names.split()
            while (names.find("  ")>=0):
                names = names.replace("  "," ")
        
            with open("friends.txt","w") as file:
                names = input("Enter your friends: ")
            if names == "":
                break
            names = names.strip()
            lnames = names.split()
            while (names.find("  ")>=0):
                names = names.replace("  "," ")

                
                '''append mode'''


        elif var == "a":
            names = input("Enter your friends: ")
            if names == "":
                break
            names = names.strip()
            lnames = names.split()
            while (names.find("  ")>=0):
                names = names.replace("  "," ")
        
            with open("friends.txt","a") as file:
                names = input("Enter your friends: ")
            if names == "":
                break
            names = names.strip()
            lnames = names.split()
            while (names.find("  ")>=0):
                names = names.replace("  "," ")
            
        elif var == "q":
            print("quit")
            break

        else:
            print("input must be like \' a\'\' w\'\' r\'")

            #str1 =file.readline()
            #while str1:
            #    str1 = file.readline()
            #    print(str1,end="")
            
            
    print("Goodbay!") 

if __name__ == "__main__":
    main()