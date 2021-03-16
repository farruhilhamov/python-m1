#!/usr/bin/env/ python3

def main():
   global wf
   filename="friends.txt"
   while (True):
      names=input("Enter your friends:")
      if names=="":
         break
      #names=names.strip()
      #while (names.find("  ")>=0):
      #   names=names.replace("  "," ")
      lnames=names.split()
      names=input("Write to old file? (Y/n):")
      if (names.lower()=="y"):
         wf="a"
      else:
         wf="w"
      with open(filename,wf) as file:
         for name in lnames:
            print(name,file=file)
            #file.write(name+"\n")
      names=input("Read from file?(Y/n):")
      if (names.lower()=="y"):
         try:
            with open(filename,"r") as file:
               content=file.readlines()
               for elem in content:
                  print(elem,end="")
         except FileNotFoundError as e:
            print("Fail ne nayden pit nado menshe!")
         #str1=file.readline()
         #while str1:
         #   str1=file.readline()
         #   print(str1,end="")
   print("Goodbye! See U!")

if __name__=='__main__':
   main()