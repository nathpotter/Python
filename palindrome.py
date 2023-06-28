#/usr/bin/python

def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    temp_reverse_num = str(original_num)[::-1]
    
    print("original_num = ", original_num)
    print("temp_reverse_num = ", temp_reverse_num)
    
    reverse_num = int(temp_reverse_num)
    print("reverse_num = ", reverse_num)
    
    # check numbers
    if original_num == reverse_num:
        print("Given number is palindrome")
    else:
        print("Given number is not palindrome")


palindrome(121)
palindrome(125)
