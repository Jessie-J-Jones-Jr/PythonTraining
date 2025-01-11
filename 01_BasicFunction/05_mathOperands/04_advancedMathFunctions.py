# Importing required libraries
import random
import numpy as np
import math

# 1. round() - Rounds a floating-point number to a specified number of decimal places
number = 3.14159
rounded_number = round(number, 2)  # Rounding to 2 decimal places
print(f"Rounded: {rounded_number}")  # Output: 3.14

# 2. abs() - Returns the absolute value of a number
negative_number = -10
absolute_value = abs(negative_number)
print(f"Absolute Value: {absolute_value}")  # Output: 10

# 3. pow() - Raises a number to the power of another number
result = pow(2, 3)  # 2 raised to the power of 3
print(f"2^3 = {result}")  # Output: 8

# 4. min() and max() - Find the smallest and largest number from a sequence
numbers = [1, 2, 3, 4]
print(f"Min value: {min(numbers)}")  # Output: 1
print(f"Max value: {max(numbers)}")  # Output: 4

# 5. sum() - Returns the sum of all items in an iterable
total = sum(numbers)  # Sum of elements in the list
print(f"Sum of list: {total}")  # Output: 10

# 6. math.sqrt() - Returns the square root of a number
square_root = math.sqrt(16)  # Square root of 16
print(f"Square root of 16: {square_root}")  # Output: 4.0

# 7. math.factorial() - Returns the factorial of a number
factorial_result = math.factorial(5)  # 5! = 5 * 4 * 3 * 2 * 1
print(f"Factorial of 5: {factorial_result}")  # Output: 120

# 8. math.ceil() - Returns the smallest integer greater than or equal to the number
ceil_value = math.ceil(2.3)  # Round up to the nearest integer
print(f"Ceiling of 2.3: {ceil_value}")  # Output: 3

# 9. math.floor() - Returns the largest integer less than or equal to the number
floor_value = math.floor(2.7)  # Round down to the nearest integer
print(f"Floor of 2.7: {floor_value}")  # Output: 2

# 10. math.pi - Constant value of Pi
pi_value = math.pi
print(f"Value of Pi: {pi_value}")  # Output: 3.141592653589793

# 11. math.sin(), math.cos(), math.tan() - Trigonometric functions
angle_in_radians = math.radians(90)  # Convert degrees to radians
print(f"Sine of 90°: {math.sin(angle_in_radians)}")  # Output: 1.0

# 12. math.radians() - Converts degrees to radians
angle_degrees = 90
angle_in_radians = math.radians(angle_degrees)
print(f"90° in radians: {angle_in_radians}")  # Output: 1.5707963267948966

# 13. random.randint() - Returns a random integer within a given range
random_integer = random.randint(1, 10)  # Random integer between 1 and 10
print(f"Random integer: {random_integer}")  # Output: Random number between 1 and 10

# 14. random.random() - Returns a random floating-point number between 0.0 and 1.0
random_float = random.random()  # Random float between 0 and 1
print(f"Random float: {random_float}")  # Output: Random float between 0 and 1

# 15. random.choice() - Returns a randomly selected item from a list
items = [1, 2, 3, 4]
random_choice = random.choice(items)  # Randomly select an item from the list
print(f"Random choice: {random_choice}")  # Output: Random item from the list

# 16. random.uniform() - Returns a random floating-point number within a specified range
random_range_float = random.uniform(1.5, 3.5)  # Random float between 1.5 and 3.5
print(f"Random float between 1.5 and 3.5: {random_range_float}")  # Output: Random number between 1.5 and 3.5

# 17. numpy.array() - Creates a numpy array
arr = np.array([1, 2, 3, 4])
print(f"NumPy array: {arr}")  # Output: [1 2 3 4]

# 18. numpy.mean() - Calculates the mean (average) of a list or array
mean_value = np.mean(arr)  # Mean of the array
print(f"Mean of array: {mean_value}")  # Output: 2.5

# 19. numpy.std() - Calculates the standard deviation of an array
std_deviation = np.std(arr)  # Standard deviation of the array
print(f"Standard deviation of array: {std_deviation}")  # Output: 1.118033988749895

# 20. random.seed() - Initializes the random number generator with a specific seed
random.seed(42)  # Initialize random number generator with a specific seed
print(f"Random number with seed 42: {random.randint(1, 100)}")  # Output: 82 (same result each time with the same seed)
