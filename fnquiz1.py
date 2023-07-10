import sys

def display(**kwargs):
    for i in kwargs:
        print(i)
        print(kwargs[i])

display(emp="Kelly", salary=9000)

sys.stderr.write('Warning, log file not found starting a new one\n')
