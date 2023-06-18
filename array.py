from array import *

array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
    #print(x)

#Solution for array code problem 1
import array as arr

i = 0
x = arr.array('i', range(1, 11))
y = arr.array('i', [0,0,0])

while i < 3:
  n = int(input('Enter number: '))
  x.append(n)
  y[i] = x.index(n) 
  i = i + 1

print(x)
print(y)
