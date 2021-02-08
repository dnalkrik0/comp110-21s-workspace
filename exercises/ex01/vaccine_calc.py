"""A vaccination calculator."""

__author__ = "730391530"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

today: datetime = datetime.today()

population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent: int = int(input("Target percent vaccinated: "))

step_one: float=(target_percent/100)
step_two: int=(2*population)
step_three: int= round(step_one * step_two)
step_four: int= step_three - doses_administered
step_five: int= round(step_four/doses_per_day)

days_passed: timedelta=timedelta(step_five)
projected_date: datetime= today + days_passed

string_target_percent: str= str(target_percent)
string_step_five: str= str(step_five)
string_projected_date: str= str(projected_date.strftime("%B %d, %Y"))

print("We will reach " + string_target_percent + "% vaccination in " + string_step_five + " days, which falls on " + string_projected_date +".")

