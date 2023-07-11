import datetime
import calendar

def detect_Friday_13(year,month):
    #Get the thirteen day of the month
    day_13_of_the_month = datetime.date(year,month,13)
    print("The thirteenth day of month {} and year {} is a {}.".format(month,year,day_13_of_the_month.strftime("%A"))) 
    if day_13_of_the_month.weekday() == 4:
       return True
    return False

ord = input("Start program to check 13th Fri? (y or n): ")

if(ord == "y"):
  m=input("Input month <eg., 01 = Jan> : ")
  y=input("Input year <eg., 1989, 2023>: ")
  while(ord != "n"):
    mo = int(m)
    ye = int(y)
    if(detect_Friday_13(year=ye,month=mo)):
      print("This month", mo, "of year", ye, "has 13th Friday")
    else:
      print("This month", mo, "of year", ye, "has NO 13th Friday")

    ord = input("Start program to check 13th Fri? (y or n): ")
    if(ord == "y"):
      m=input("Input month <eg., 01 = Jan> : ")
      y=input("Input year <eg., 1989, 2023>: ")
