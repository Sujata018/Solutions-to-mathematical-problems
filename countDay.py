day=18
month=4
year=2001
WeekDay=3

count=0
while True:
    if (day == 13) and (WeekDay==1):
        count += 1
    if (day==12) and (month==2) and (year==2099):
        break
    if ((day == 30) and (month in [4,6,9,11])) or ((day ==31) and month in [1,3,5,7,8,10]) or ((month==2) and (day==29) and (year%4==0)) or ((month==2) and (day==28) and (year%4!=0)):
        day=1
        month += 1
    elif (day==31) and (month==12):
        day = 1
        month = 1
        year += 1
    else :
        if WeekDay==6:
            WeekDay = 0
        else:
            WeekDay += 1
        day += 1
print('count=',count)
    
