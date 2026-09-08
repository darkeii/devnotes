import datetime

from sympy.printing.octave import print_octave_code

date = datetime.date(2025,8,10)              # year/month/date
today = datetime.date.today()               # today's date

time = datetime.time(12,30,0)
now = datetime.datetime.now()               # current time

# https://docs.python.org/3/library/datetime.html

now = now.strftime("%H:%M:%S  %d-%m-%Y")        # "%" = format specifiers

print(date)
print(today)
print(time)
print(now)

#--------------------------------------------------------------------------
# Exercise = checking if the current date and time has passed the target_datetime

target_datetime = datetime.datetime(2020, 1, 2, 12, 30, 1)          # in its parameter arguments are = (date(YYYY/M/D) , time(Hour/Mins/seconds))
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")


