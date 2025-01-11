# 1. 
# data = [1, 2, 3]
# print(data + "4")
# Corrected: print(data + [4])
# Explanation: You cannot add a list and a string together. The correct way to add an element to a list is to append it or add a list containing the element. Here, `[4]` is used instead of the string `"4"` to ensure type compatibility.

# 2.
# result = "5" * 3.0
# print(result)
# Corrected: result = "5" * int(3.0)
# Explanation: The `*` operator for strings requires an integer, not a float. To fix the issue, we convert `3.0` to an integer using `int()`.

# 3.
# a = "100"
# b = 200
# print(a * b)
# Corrected: print(int(a) * b)
# Explanation: The string `"100"` cannot be multiplied by an integer directly. To multiply, we need to convert the string to an integer using `int(a)` before performing the operation.

# 4.
# lst = [1, 2, 3]
# print(lst["1"])
# Corrected: print(lst[1])
# Explanation: List indices must be integers, not strings. The correct way to access the second element in the list is using the index `1`, not the string `"1"`.

# 5.
# def add(a, b):
#     return a + b
# print(add("Hello", [1, 2]))
# Corrected: print(add("Hello", str([1, 2])))
# Explanation: You can't directly add a string and a list. In this case, the solution is to convert the list to a string using `str()`, which will concatenate it with the string `"Hello"`.

# 6.
# name = "Alice"
# print(name[10])
# Corrected: print(name[4])  # Example of valid index
# Explanation: The string `"Alice"` has only 5 characters (index 0 to 4). Trying to access `name[10]` results in an "index out of range" error. We change it to a valid index like `name[4]`.

# 7.
# value = [1, 2, 3]
# print(value + None)
# Corrected: print(value + [None])
# Explanation: You can't add a list and `None` directly. The correct way is to wrap `None` in a list (`[None]`) to concatenate it with the `value` list.

# 8.
# x = 10
# print(x + None)
# Corrected: print(x + 0)  # or another valid fallback value for None
# Explanation: You cannot add `None` to an integer. If `None` is expected, you need to handle it with a fallback value such as `0`.

# 9.
# print("Value is: " + None)
# Corrected: print("Value is: " + str(None))
# Explanation: The `+` operator in Python requires both operands to be strings, so we convert `None` to a string using `str()`.

# 10.
# dict_obj = {1: "a", 2: "b"}
# print(dict_obj[None])
# Corrected: print(dict_obj.get(1))  # or another valid key
# Explanation: In the dictionary, `None` is not a valid key, and attempting to access it will result in a `KeyError`. We should use a valid key (like `1` or `2`), or use `dict_obj.get(key)` to handle missing keys safely.

# 11.
# a = 5
# b = "10"
# print(f"Sum: {a} + {b} = {a + b}")
# Corrected: print(f"Sum: {a} + {b} = {a + int(b)}")
# Explanation: `b` is a string, so we need to convert it to an integer before adding it to `a`. We use `int(b)` to ensure both values are integers.

# 12.
# num = 10
# print(len(num))
# Corrected: print(len(str(num)))
# Explanation: The `len()` function requires a sequence (like a string or list), but `num` is an integer. We convert it to a string using `str()` before passing it to `len()`.

# 13.
# result = 5 ** "2"
# print(result)
# Corrected: result = 5 ** int("2")
# Explanation: The exponentiation operator (`**`) requires both operands to be numbers. We need to convert the string `"2"` to an integer using `int()`.

# 14.
# def test_func(a, b):
#     return a + b
# print(test_func("text", 10.5))
# Corrected: print(test_func("text", str(10.5)))
# Explanation: You can't add a string and a float directly. In this case, we convert the float to a string to perform the concatenation.

# 15.
# x = {1, 2, 3}
# y = [4, 5, 6]
# print(x + y)
# Corrected: print(list(x) + y)
# Explanation: You cannot add a set and a list. To combine them, we convert the set `x` to a list using `list(x)` and then add the two lists together.
