#!/usr/bin/env/ python3

def main():
    action = input("decode or encode(last word) , (y/n): ")
    s = int(input("enter sdvig: "))
    global alph
    global nextword
    global gen
    nextword = []
    #global doc
    gen = ''
    alph = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","j","J","i","I","k","K","l","m","M","n","N","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","w","W","x","X","y","Y","z","Z"]
    
    def decode(word):
        
        doc = open("coder.txt", "w+")
        liwor = list(myword)
        for i in liwor:
            if i == i.lower:
                l = alph.index(i)
                if alph [l] != 'z':

                    doc.write(alph [l+s+2])

                else:
                    doc.write(alph [0])  
            else:
                l = alph.index(i)
                if alph [l] != 'Z':
                    '''доделать высокие символы'''
                    if alph [l] == 'z':
                        doc.write(alph[0])
                    doc.write((alph [l+s+2]))
                else:
                    doc.write(alph [1])  
                
        doc = open("coder.txt","r")
        pr = (doc.readlines(0)) 
        pr = pr [0]
        print(pr)

        #doc = open("coder.txt", "a")
        #doc.write("\n")
        return nextword
    def uncode(word):
        doc = open("coder.txt", "r")
        uncow = list(doc.readlines())
        uncow = list(uncow[0])
        uncoded = ''
        for i in uncow:
            l = alph.index(i)

            if alph [l] == "A":    
                uncoded += "Z"
            
            elif alph [l] == "a":
                uncoded += "z"

            elif alph[l] != "A":
                uncoded += alph [ l - s-2]
            
        print(uncoded)    
        return nextword,uncow,uncoded
    if action == 'y':
        myword = input("enter your word: ")
        decode(myword)
    elif action == 'n':
        uncode("")
    else:
        print("error")
    
    
    


if __name__ == "__main__":
    main()