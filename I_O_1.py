num = 33
print('%o' %num)

num = 458.541315
print('%.3f' % num)

numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
#    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

#print("User List:", numbers)

str1, str2, str3 = input("Enter three string: ").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)
