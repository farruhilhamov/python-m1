#!/usr/bin/env/ python3
from datetime import datetime as dt

def main():
    date = dt.now()
    year = date.year
    gyear = 365.2425
    visdni = 0
    month = date.month
    day = date.day
    thisdays = ((month * 31) - 31 + day)
    for i in range(year - 1600):
        if i % 4 == 0:
            visdni += 4
    print("reznica v nastoyashee vremya v dnyah: ",year * gyear + visdni - year * 365 + thisdays )
    


if __name__ == "__main__":
    main()
