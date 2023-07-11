import datetime
def has_friday_13(month,year):
    return datetime.date(year,month,13).strftime("%A")== "Friday"
month=int(input("month:"))
year=int(input("year:"))
print(has_friday_13(month,year))
