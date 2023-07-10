

#strr = "Programm"

strr = input("Enter a string: ")

# empty dictionary
dic = {}

for ele in strr:
    if ele in dic:
        dic[ele] += 1
    else:
        dic[ele] = 1

# result
print("Occurrence of each characters is :\n " + str(dic))

# String initialization
n = '@pyThOnlobb!Y34'
numeric = 0
lower = 0
upper = 0
special = 0

for i in range(len(n)):
    if n[i].isnumeric():
        numeric = numeric + 1
    elif n[i].islower():
        lower = lower+1
    elif n[i].isupper():
        upper = upper+1
    else:
        special = special + 1

# printing result
print("Numeric counts",numeric)
print("Lower counts",lower)
print("Upper counts",upper)
print("Special counts",special)
