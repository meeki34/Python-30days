# how to use the date moduel in python

import datetime

date = datetime.date(2025, 9, 12)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2025, 12, 31, 23, 59, 59)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("The target date and time has passed.")
else:
    time_difference = target_datetime - current_datetime
    print(f"Time difference: {time_difference}")

print(now)
print(time)
print(date)
print(today)
print(today.year)
print(today.month)
print(today.day)