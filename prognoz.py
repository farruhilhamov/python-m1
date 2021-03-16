#!/usr/bin/env/ python3
import math
from datetime import datetime as dt

def main():
    acity = {"tashkent" : 'hot',
             "moscow" : 'cold',
             "london": 'cloudy',
             "paris": 'lovely',
             "tambov": 'Buhlo',
             "tokyo": 'rain'
            }
    while True:
        isFind = False
        city = input("Enter your city: ")
        if (city == ''):
            break
        city = city.lower()
        for key in acity.keys() :
            if city == key [0:len(city)]:
                print(acity [key])
                isFind = True
        if isFind == False:
            print("i dont undestand you")
        #if city == acity[0] [0] [0:len(city)]:
        #    print(acity[0] [1])
        #elif city == acity[1] [0]  [0:len(city)]:
        #    print(acity[2] [0])
        #elif city == acity[2] [1] [0:len(city)]:
        #    print(acity[2] [1] )
        #elif city == acity[3] [0] [0:len(city)]:
        #    print(acity[3] [1])
        #elif city == acity[4] [0] [0:len(city)]:
        #    print(acity[4] [1])
        #else:
        #    print("i dont udershvohen!")

    print("Goodbay!")
if __name__ == "__main__":
    main()