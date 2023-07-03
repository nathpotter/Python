#/usr/bin/python
from decimal import *

taxes = [
    { "max": Decimal(150000), "rate": Decimal(0.00) },
    { "max": Decimal(300000), "rate": Decimal(0.05) },
    { "max": Decimal(500000), "rate": Decimal(0.10) },
    { "max": Decimal(1000000), "rate": Decimal(0.20) },
    { "max": Decimal(2000000), "rate": Decimal(0.25) },
    { "max": Decimal(5000000), "rate": Decimal(0.30) },
    { "max": None,    "rate": Decimal(0.35) }
]

value = input("Enter your annual salary (q to quit): ")
while value != 'q':
    salary = Decimal(value)
    previous_step_max = Decimal(0)
    tax = Decimal(0)
    is_last_step = False

    for t in taxes:

        # If max is None, then it is last steps
        if t['max'] == None:
            print("Step {0:,}".format(previous_step_max), end='')
            step_tax = salary * t['rate']
            tax += step_tax

        else:
            print("Step {0:,}-{1:,}".format(previous_step_max, t['max']), end='')
            range = t['max'] - previous_step_max

            if salary > range:
                step_tax = range * t['rate']
                tax += step_tax

                salary -= range
                previous_step_max = t['max']

            else:
                step_tax = salary * t['rate']

                tax += step_tax
                is_last_step = True

        print(" (rate: ", round(t['rate'],2) , "%) => Tax: {0:,}".format(round(step_tax, 2)))
        if is_last_step:
            break

    print()
    print("Total tax: {0:,}".format(round(tax, 2)))
    value = input("Enter your annual salary (q to quit): ")
