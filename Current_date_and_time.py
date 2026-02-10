from  datetime import date , time , datetime

today = date.today()
now = datetime.now()
print("Today's date is ",today)
print("\n Current date and time is ", now)


print("\n Date componets" ,today.year , today.month , today.day)