def character_generator(word_list):
    for word in word_list:
        for ch in word:
            yield ch

from array import *

test_four = array("u", character_generator(["Test","One","Two"]))
for i in test_four:
    print(i)


test_str = array("u", ["Test","One","Two"])
print(test_four)
print(test_str)
