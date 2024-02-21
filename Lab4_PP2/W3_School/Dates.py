import datetime

time = datetime.datetime.now()
print(time)
print(time.year)
print(time.strftime("%A"))

time2 = datetime.datetime(2020, 3, 18)
print(time2)

time3 = datetime.datetime(2015, 5, 3)
print(time3.strftime("%B"))