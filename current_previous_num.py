#/usr/bin/python

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(0, 10):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i
    

# Other way of coding
previous_num = 0
i = 0
while(previous_num < 9):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    previous_num = i
    i = i + 1
