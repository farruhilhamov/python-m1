#!/usr/bin/env/ python3

from datetime import datetime as dt
     
def main():
    today = dt.now()
    date = today.day
    month = today.month
    year = today.year
    second = today.second
    minute = today.minute
    hour = today.hour
    m = "0" + str(month) if (month<10) else str(month)
    
    '''здесь начало конвертирования'''
    if len(str(second)) ==1:
        second = "0"+str(second)
    if len(str(minute)) ==1:
        minute = "0"+str(minute)
    if len(str(hour)) ==1:
        hour = "0"+str(hour)


    print("-"*12)
    print(date,month,year,sep='.')
    '''здесь сепарация'''
    print(hour,minute,second,sep=":")
     
    print('-'*12)
    if 1 <= date<=10:
        print('Milk')
    elif 11<= date <=20:
        print("meat")
    elif 21<=date<=25:
        print("alcohol")
    else: 
        print("parfume") 

    




if __name__ == "__main__":
    main()    