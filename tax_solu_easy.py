#/usr/bin/python
from decimal import *

tax1 = 0
tax2 = 7500
tax3 = 20000
tax4 = 37500
tax5 = 50000
tax6 = 250000
tax7 = 900000

value = input("Enter your annual salary (q to quit): ")

while value != 'q':
    
    #month_salary = int(value)
    #salary = int(month_salary*12)
    salary = int(value)
    print("Annual salary: ", salary)
    total_tax = 0
    temp = 0
    
    #Level1
    if(salary <= 150000):
        total_tax = tax1
    #Level2
    elif(salary <= 300000):
        temp = salary - 150000
        total_tax = temp * 0.05
    #Level3
    elif(salary <= 500000):
        temp = salary - 300000
        total_tax = tax2 + (temp * 0.10)
    #Level4
    elif(salary <= 750000):
        temp = salary - 500000
        total_tax = tax2 + tax3 + (temp * 0.15)
    #Level5
    elif(salary <= 1000000):
        temp = salary - 750000
        total_tax = tax2 + tax3 + tax4 + (temp * 0.20)
    #Level6
    elif(salary <= 2000000):
        temp = salary - 1000000
        total_tax = tax2 + tax3 + tax4 + tax5 + (temp * 0.25)
    #Level7
    elif(salary <= 5000000):
        temp = salary - 2000000
        total_tax = tax2 + tax3 + tax4 + tax5 + tax6 + (temp * 0.30)
    #Level8
    else:
        temp = salary - 5000000
        total_tax = tax2 + tax3 + tax4 + tax5 + tax6 + tax7 + (temp * 0.35)
        
    print()
    print("Total tax: ", total_tax)
    value = input("Enter your annual salary (q to quit): ")
