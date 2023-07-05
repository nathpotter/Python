def fn_hello():
  print("hello")

def my_function1(fname):
  print(fname + " Test")
  
def my_function2(fname, lname):
  print(fname + " " + lname)

#called function will received Tuples
def my_function3(*kids):
  print("The youngest child is ", kids[2])
  
def my_function4(child3, child2, child1):
  print("The youngest child is " + child2)
  
def my_function5(country = "Norway"):
  print("I am from " + country)

#called function will received Dict.
def my_function6(**kid):
  print("His fore name is " + kid["fname"])
  print("His last name is " + kid["lname"])
  
#duplicate function
def my_function7():
 print("dup function")

def print_list(food):
  for x in food:
    print(x)
    
def expo(x):
    return x * x
    
def print_multiple_table():
    pass
################################################################
fn_hello()

################################################################
my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

################################################################
my_function2("Emil", "Refsnes")

################################################################
my_function3("Emil", "Tobias", "Linus")

################################################################
my_function4(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
################################################################
my_function5("Sweden")
my_function5("India")
my_function5()
my_function5("Brazil")
################################################################
my_function6(fname = "Tobias", lname = "Refsnes")
my_function7()
################################################################
fruits = ["apple", "banana", "cherry"]
print_list(fruits)
################################################################
print(expo(3), expo(4), expo(5))
print_multiple_table()
################################################################
