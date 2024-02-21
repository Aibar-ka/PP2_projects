Exercise: 1
from datetime import datetime, timedelta

current_date = datetime.now()

result_date = current_date - timedelta(days=5)

print(result_date.strftime("%Y-%m-%d"))


Exercise: 2

today = datetime.now()

yesterday = today.replace(day=today.day - 1)
tomorrow = today.replace(day=today.day + 1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))


Exercise: 3
current_datetime = datetime.now()

microseconds = current_datetime.replace(microsecond=0)

print(microseconds)


Exercise: 4
date1 = datetime(2024, 2, 20, 12, 0, 0)  # Example date 1
date2 = datetime(2023, 5, 11, 3, 23, 34)  # Example date 2

time_minus = date1 - date2

difference_in_seconds = time_minus.total_seconds()


print("time_minus:", difference_in_seconds)