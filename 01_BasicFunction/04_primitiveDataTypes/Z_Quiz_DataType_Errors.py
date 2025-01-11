# Remove the "#" in front of the function
# Paste the error above the issue. 
# Recomment Out the function. 
# Fix the issues below each problematic line. 

# 1. TypeError: object of type 'int' has no len()
#print(len(12345))
print(len( str(12345)))


# 2. TypeError: can only concatenate str (not "int") to str
#print("The number is: " + 42)
print("The number is: " + str(42))



# 3. TypeError: 'int' object is not iterable
#for char in 1234:
#print(char)


for char in str(1234):
    print(char)


# 4. TypeError: unsupported operand type(s) for +: 'int' and 'str'
#total = 10 + "20"
#print(total)

#You have to choose which you want to do with the operand.
total = "10" + "20"
print(total)


#Or 

total = 10 + int("20")
print(total)

# 5. TypeError: must be real number, not str
#import math
#print(math.sqrt("16"))

import math
print(math.sqrt(int("16")))

# 6.TypeError: 'int' object is not subscriptable
#num = 12345
#print(num[0])

num = str(12345)
print(num[0])

# 7. TypeError: can't multiply sequence by non-int of type 'str'
#result = "Hi" * "5"
#print(result)

#Solution change operand if concantenation is the goal 
result = "Hi" + "5"
print(result)

#Or change to integer if you wanted to true multiply the str multiple times
result = "Hi" * 5
print(result)


# 8. TypeError: 'float' object cannot be interpreted as an integer
#for i in range(5.0):
#print(i)


for i in range(int(5.0)):
    print(i)


# 9. No error just not good practice
#length = len
#print(length([1, 2, 3]))

#Not a good idea to rename the embedded functions.
print(len([1, 2, 3]))

# 10. IndexError: Replacement index 1 out of range for positional args tuple
#print("The value of x is: {} and y is: {}".format(10))

print("The value of x is: {} and y is: {}".format(10, 20))

# 11. Traceback (most recent call last): KeyError: 0
#data = {"key": "value"}
#print(data[0])

data = {"key": "value"}
print(data["key"])


# 12. TypeError: can only concatenate str (not "int") to str
#x = "10"
#y = x + 5
#print(y)

x = "10"
y = int(x) + 5
print(y)

# 13. TypeError: list indices must be integers or slices, not str
#lst = [1, 2, 3]
#print(lst["0"])

lst = [1, 2, 3]
print(lst[int("0")])


# 14. TypeError: unsupported operand type(s) for /: 'int' and 'str'

#print(3 / "3")
print(3 / int("3"))

# 15. ValueError: invalid literal for int() with base 10: 'abc'
#print(int("abc"))
print(int("123"))

# 16. TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

#def func():
#    return 
#print(func() + 10)

#Solution 1 func has to return a value (if necessary value has to be turned into 
# an integer if the operand is to work#)
def func():
    return 1
print(func() + 10)

#Solution 2 change operand to one that can deal with a None data type
def func():
    return
print(func() or 10)


# 17. TypeError: can only concatenate str (not "int") to str
#float_value = "123.45"
#print(float_value + 10)

float_value = float("123.45")
print(float_value + 10)

# 18. TypeError: unsupported operand type(s) for -: 'str' and 'int'
#result = "10" - 5
#print(result)

result = int("10") - 5
print(result)

# 19. TypeError: unsupported operand type(s) for +: 'int' and 'str'
#x = 20
#y = int("30")
#print(x + y)

x = 20
y = int("30")
print(x + y)


# 20.IndexError: list index out of range

#lst = [1, 2, 3]
#print(lst[5])

#Solution 1 extend list for the 6th indexed value [5] is the 6th because the 
# index starts with 0#
lst = [1, 2, 3]
lst.extend([4, 5, 6])
print(lst[5])

#Solution 2 change the index value#
lst = [1, 2, 3]
print(lst[2])

# 21. TypeError: must be real number, not str
#import math
#print(math.pow("2", 3))

import math
print(math.pow(int("2"), 3))

# 22. TypeError: must be real number, not str
#name = "John"
#print(name + 25)

name = "John"
print(name + str(25))

# 23. TypeError: can only concatenate str (not "int") to str
name = "Alice"
age = "25"
print("Name: " + name + ", Age: " + age + ", Next year: " + str((int(age) + 1)))

#name = "Alice"
#age = "25"
#print("Name: " + name + ", Age: " + age + ", Next year: " + age + 1)

# 24. TypeError: can only concatenate str (not "int") to str

def add_numbers(a , b):
    return a + str(b)
print(add_numbers("Hello", 5))

#def add_numbers(a, b):
#  return a + b
#print(add_numbers("Hello", 5))

# 25.
number = 10
result = str(number) + "abc"
print(result)

#number = 10
#result = number + "abc"
#print(result)

# 26. TypeError: list indices must be integers or slices, not str
a = [1, 2, 3]
print(a[1])

#a = [1, 2, 3]
#print(a["1"])

# 27.
age = "20"
print(int(age))

#age = "twenty"
#print(int(age))

# 28.
data = ["a", "b", "c"]
print(data + [5])

#data = ["a", "b", "c"]
#print(data + 5)

# 29. TypeError: can't multiply sequence by non-int of type 'str'
value = "123"
print(value * int("10"))

#value = "123"
#print(value * "10")


# 30.TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
x = None
print(str(x) + str(10))

#x = None
#print(x + 10)

