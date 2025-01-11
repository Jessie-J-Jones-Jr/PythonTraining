# 1. 
# len(12345)
# Corrected: len(str(12345))
# Reason: len() works only on sequences (like strings, lists), so we convert the integer to a string.

# 2.
# print("The number is: " + 42)
# Corrected: print("The number is: " + str(42))
# Reason: We need to convert the integer to a string to concatenate with other strings.

# 3.
# for char in 1234:
#     print(char)
# Corrected: for char in str(1234): print(char)
# Reason: We need to iterate over a string, so we convert the number to a string.

# 4.
# total = 10 + "20"
# Corrected: total = 10 + int("20")
# Reason: You can't add an integer and a string, so convert the string to an integer.

# 5.
# import math
# print(math.sqrt("16"))
# Corrected: print(math.sqrt(int("16")))
# Reason: math.sqrt() requires a number, so we need to convert the string to an integer.

# 6.
# num = 12345
# print(num[0])
# Corrected: print(str(num)[0])
# Reason: Integers aren't subscriptable, so convert the number to a string first.

# 7.
# result = "Hi" * "5"
# Corrected: result = "Hi" * 5
# Reason: We can't multiply a string by another string; the multiplier must be an integer.

# 8.
# for i in range(5.0):
#     print(i)
# Corrected: for i in range(int(5.0)): print(i)
# Reason: range() only accepts integers, so we convert the float to an integer.

# 9.
# length = len
# print(length([1, 2, 3]))
# Corrected: print(len([1, 2, 3]))
# Reason: `len` is a function, not a variable. We call it directly.

# 10.
# print("The value of x is: {} and y is: {}".format(10))
# Corrected: print("The value of x is: {} and y is: {}".format(10, 20))
# Reason: We need to provide two arguments for both placeholders in the format string.

# 11.
# data = {"key": "value"}
# print(data[0])
# Corrected: print(data["key"])
# Reason: Dictionaries use keys for indexing, not integers.

# 12.
# x = "10"
# y = x + 5
# Corrected: y = int(x) + 5
# Reason: We can't add a string and an integer, so we convert the string to an integer.

# 13.
# lst = [1, 2, 3]
# print(lst["0"])
# Corrected: print(lst[0])
# Reason: List indices must be integers, so we use 0 instead of the string "0".

# 14.
# print(3 / "3")
# Corrected: print(3 / int("3"))
# Reason: We need to convert the string "3" to an integer to perform the division.

# 15.
# print(int("abc"))
# Corrected: print(int("123"))
# Reason: "abc" is not a valid integer string. We use a valid integer string, like "123".

# 16.
# def func():
#     return
# print(func() + 10)
# Corrected: print(func() or 10)
# Reason: The function returns None, so we handle it with a fallback value (10).

# 17.
# float_value = "123.45"
# print(float_value + 10)
# Corrected: print(float(float_value) + 10)
# Reason: We need to convert the string "123.45" to a float before adding 10.

# 18.
# result = "10" - 5
# Corrected: result = int("10") - 5
# Reason: We need to convert "10" to an integer to perform the subtraction.

# 19.
# x = 20
# y = "30"
# print(x + y)
# Corrected: print(x + int(y))
# Reason: We need to convert the string "30" to an integer before performing the addition.

# 20.
# lst = [1, 2, 3]
# print(lst[5])
# Corrected: print(lst[2])  # Example of valid index
# Reason: Index 5 is out of range, so use an index within the valid range (e.g., 2).

# 21.
# import math
# print(math.pow("2", 3))
# Corrected: print(math.pow(2, 3))
# Reason: `math.pow()` expects numbers, not strings, so we pass integers directly.

# 22.
# name = "John"
# print(name + 25)
# Corrected: print(name + str(25))
# Reason: We need to convert the integer 25 to a string before concatenation.

# 23.
# name = "Alice"
# age = "25"
# print("Name: " + name + ", Age: " + age + ", Next year: " + age + 1)
# Corrected: print(f"Name: {name}, Age: {age}, Next year: {int(age) + 1}")
# Reason: We need to convert age to an integer to add 1, and use f-strings for easier formatting.

# 24.
# def add_numbers(a, b):
#     return a + b
# print(add_numbers("Hello", 5))
# Corrected: print(add_numbers("Hello", str(5)))
# Reason: You cannot add a string and an integer, so we ensure both are strings.

# 25.
# number = 10
# result = number + "abc"
# print(result)
# Corrected: result = str(number) + "abc"
# Reason: We need to convert the integer to a string before concatenation.

# 26.
# a = [1, 2, 3]
# print(a["1"])
# Corrected: print(a[1])
# Reason: List indices must be integers, not strings.

# 27.
# age = "twenty"
# print(int(age))
# Corrected: age = "20"  # If the age is a string, ensure it's a valid integer string
# Reason: The string "twenty" is not a valid integer.

# 28.
# data = ["a", "b", "c"]
# print(data + 5)
# Corrected: print(data + ["d", "e", "f"])
# Reason: You cannot add a list and an integer. Instead, add a list to another list.

# 29.
# value = "123"
# print(value * "10")
# Corrected: print(int(value) * 10)
# Reason: The multiplication operator expects an integer on both sides, so convert the string to an integer.

# 30.
# x = None
# print(x + 10)
# Corrected: print(10 if x is None else x + 10)
# Reason: You cannot add `None` to an integer, so we handle it with a conditional fallback value.
