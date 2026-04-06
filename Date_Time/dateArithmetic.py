from datetime import datetime, timedelta, date

now = datetime.now()              # current date & time

gap = timedelta(days=3)           # create 3-day duration

future = now + gap                # move forward
past = now - gap                  # move backward

print("Now:", now)
print("After 3 days:", future.date())
print("3 days ago:", past.date())