#/usr/bin/python

print("list(range(0, 10, 3)): ", list(range(0, 10, 3)))
print("list(range(-10, -100, -30)) ", list(range(-10, -100, -30)))

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Size: ", size)
print("Printing only even index chars")
for i in range(0, size, 2):
    print("index[", i, "]", word[i])
    
    
# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in word[0::2]:
    print(i)
    
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
