#!/usr/bin/env/ python3

def encrypt(pstr,poffset):
   str_total=""
   for ch in pstr:
      str_total+=chr(ord(ch)+poffset)
   return str_total

def main():
   string=input("Enter your string for encrypt: ")
   secret_word=input("Enter your secret word for encrypt: ")
   offset=int(input("Enter your offset:"))
   with open("data.enc","w") as f:
      f.write(encrypt(string,offset)+"\n")
      f.write(secret_word+"="+encrypt(secret_word,offset))
   with open("data.enc","r") as file:
      string=file.readline()
      secret_word=file.readline()
   string=string[:-1]
   sw_enc=secret_word.split("=")
   isTrue=True
   while(isTrue):
      offset=int(input("Enter your offset for deencrypt: "))
      if (sw_enc[0]==encrypt(sw_enc[1],offset*-1)):
         isTrue=not isTrue
         print(encrypt(string,offset*-1))

   
   
if __name__=='__main__':
   main()