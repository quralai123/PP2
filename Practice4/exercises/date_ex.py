#ex1
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print(current_date)
print(new_date)

#ex2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday.date())
print(today.date())
print(tomorrow.date())

#ex3
from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print(now)
print(without_microseconds)

#ex4
from datetime import datetime

date1 = datetime(2025, 2, 20, 12, 0, 0)
date2 = datetime(2025, 2, 25, 12, 0, 0)

difference = date2 - date1
print(int(difference.total_seconds()))

