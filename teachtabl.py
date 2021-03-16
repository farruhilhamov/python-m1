#!/usr/bin/env/ python3
import math

def main():
   while True:
      imin1=0
      imax1=0
      imin2=0
      imax2=0
      smin1=input("Please enter first minimum:")
      if (smin1==''):
         break
      else:
         imin1=int(smin1)
      smax1=input("Please enter first maximum:")
      if (smax1==''):
         continue
      else:
         imax1=int(smax1)
      smin2=input("Please enter second minimum:")
      if (smin2==''):
         continue
      else:
         imin2=int(smin2)
      smax2=input("Please enter second maximum:")
      if (smax2==''):
         continue
      else:
         imax2=int(smax2)
      s=""
      for i in range(imin1,imax1):
         for j in range(imin2,imax2):
            s=s+str(j)+' x '+str(i)+' = '+str(round(math.sqrt(j*i),2))+'\t'
         print(s)
         s=''
   print("Goodbye!")

if __name__=='__main__':
   main()