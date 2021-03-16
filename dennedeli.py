#!/usr/bin/env/ python3

from calendar import weekday
from datetime import date, datetime as dt
from time import strftime
mday = int(input("enter your day of birth: "))
mmonth = int(input("enter month of tour birth: "))
myear = int(input("year: "))
now = dt.now()
month = now.month
day = now.day
year = now.year
y = myear
m = 5
d = 7
def main():
    wek = weekday(y,m,d)
    if wek == 0:
        print("пн")
    if wek == 1:
        print("вт")
    if wek == 2:
        print("ср")
    if wek == 3:
        print("чт")
    if wek == 4:
        print("пт")
    if wek == 5:
        print("сб")
    if wek == 6:
        print("вс")
if __name__ == "__main__":
    main()


