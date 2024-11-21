
from datetime import datetime, timedelta

days_to_add = 10
current_date = datetime.now()
new_date = current_date + timedelta(days=days_to_add)
print("Current Date:", current_date.date())
print("New Date:", new_date.date())
