#/usr/bin/python

def multiplication(num1, num2):
    # calculate product of two number
    return num1 * num2

def sum(num1, num2):
    # calculate product of two number
    return num1 + num2

num1 = int(input('num1: '))
num2 = int(input('num2: '))

# first condition
result = multiplication(num1, num2)
print("The result of multiplication is", result)

# Second condition
result = sum(num1, num2)
print("The result of sum is", result)
