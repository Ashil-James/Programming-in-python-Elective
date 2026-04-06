from datetime import datetime

now = datetime.now()

print("24-hour format:", now.strftime("%H:%M:%S"))
print("12-hour format:", now.strftime("%I:%M %p"))
print("Date:", now.strftime("%d-%m-%Y"))
print("Full:", now.strftime("%B, %d %A %Y %I:%M:%S %p"))