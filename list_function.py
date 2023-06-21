#/usr/bin/python

list1 = ['a', 'bbb', 'c', 'dog', 'egg']
print('before reverse', list1)
list1.reverse()
print('after reverse', list1)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print('one line code', res)

res2 = []
for x in list1:
    for y in list2:
        res2.append(x+y)
        
print('multiple line code', res2)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-2]):
    print(x, y)

list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(21)

# update item present at location
list1[index] = 200
print(list1)
