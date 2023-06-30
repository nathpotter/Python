
list = []
number = int(input("Type 4 digits number: "))

print("Given number ", number)

while number > 0:
    # get the last digit
    digit = number % 10
        
    # remove the last digit and repeat the loop
    number = number // 10
    
    list.append(digit)
    #print(digit, end=" ")
    
print('Reversed List:', list)
