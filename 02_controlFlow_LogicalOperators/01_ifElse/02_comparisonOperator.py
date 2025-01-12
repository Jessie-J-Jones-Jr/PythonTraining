# Comparison operators example

# Defining two variables
x = 5
y = 10

# 1. Equal to (==): Checks if the two values are equal
result_equal = (x == y)
print(f"x == y: {result_equal}")  # Output: False (5 is not equal to 10)

# 2. Not equal to (!=): Checks if the two values are not equal
result_not_equal = (x != y)
print(f"x != y: {result_not_equal}")  # Output: True (5 is not equal to 10)

# 3. Greater than (>): Checks if the left operand is greater than the right operand
result_greater_than = (x > y)
print(f"x > y: {result_greater_than}")  # Output: False (5 is not greater than 10)

# 4. Less than (<): Checks if the left operand is less than the right operand
result_less_than = (x < y)
print(f"x < y: {result_less_than}")  # Output: True (5 is less than 10)

# 5. Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand
result_greater_equal = (x >= y)
print(f"x >= y: {result_greater_equal}")  # Output: False (5 is not greater than or equal to 10)

# 6. Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand
result_less_equal = (x <= y)
print(f"x <= y: {result_less_equal}")  # Output: True (5 is less than or equal to 10)

# Additional Example with different values
a = 7
b = 7

# Equal to (==) check for the same values
result_equal_2 = (a == b)
print(f"a == b: {result_equal_2}")  # Output: True (7 is equal to 7)

# Not equal to (!=) check for the same values
result_not_equal_2 = (a != b)
print(f"a != b: {result_not_equal_2}")  # Output: False (7 is equal to 7, so not unequal)

# Greater than (>) check with same values
result_greater_than_2 = (a > b)
print(f"a > b: {result_greater_than_2}")  # Output: False (7 is not greater than 7)

# Less than (<) check with same values
result_less_than_2 = (a < b)
print(f"a < b: {result_less_than_2}")  # Output: False (7 is not less than 7)

# Greater than or equal to (>=) with same values
result_greater_equal_2 = (a >= b)
print(f"a >= b: {result_greater_equal_2}")  # Output: True (7 is equal to 7)

# Less than or equal to (<=) with same values
result_less_equal_2 = (a <= b)
print(f"a <= b: {result_less_equal_2}")  # Output: True (7 is equal to 7)
