#!/usr/bin/env/ python3
from datetime import datetime as dt

def main():
    date = dt.now()
    seconds = date.second
    day = int(input("enter your day: "))
    month = int(input("enter your month: "))
    year = int(input("enter your year: "))
    mdate = dt(year,month,day)
    seconds = ((int(date.strftime("%Y"))*364)*24*60)
    print(date - mdate)
    print("-"*6)
    print(seconds)



if __name__ == "__main__":
    main()
    