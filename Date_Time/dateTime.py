from datetime import datetime, timedelta

now = datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Date: ", now.date())

gap = timedelta(days = 10, weeks = 5)
print((now + gap).strftime("%d %A %B %m %Y"))