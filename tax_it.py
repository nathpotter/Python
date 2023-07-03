income = int(input("Your income :"))
salary = income * 12
print("Salary: ", salary)
tax = 0
tax1 = 0
tax2 = 0
tax3 = 0
tax4 = 0
tax5 = 0
tax6 = 0
tax7 = 0
tax8 = 0
if(salary <= 150000):
    tax1 = 0
elif(salary <= 300000):
    
    x1 = salary - 150000 
    print("x1 ", x1)
    tax2 = x1 * 5 / 100
    print("tax2 ", tax2)
elif(salary<=500000):
    x2 = salary - 300000
    tax3 = x2*10 / 100
elif(salary<=750000):
    x3 = salary - 500000
    tax4 = x3*15 / 100
elif(salary<=1000000):
    x4 = salary - 750000
    tax5 = x4*20 / 100
elif(salary<=2000000):
    x5 = salary - 1000000
    tax6 = x5*25 / 100
elif(salary<=5000000):
    x6 = salary - 2000000
    tax7 = x6*30 / 100
elif(salary>500000):
    x7 = salary - 5000000
    tax8 = x7*35 / 100


print("Total tax to pay is", tax+tax1+tax2+tax3+tax4+tax5+tax6+tax7+tax8)
