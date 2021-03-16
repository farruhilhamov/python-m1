#!/usr/bin/env/ python3

#comment

def main():
   imin = int(input('min: '))
   imax = int(input('max: '))
   for i in range (imin,imax):
      print(i, i**2)

if __name__ == "__main__":
   main()