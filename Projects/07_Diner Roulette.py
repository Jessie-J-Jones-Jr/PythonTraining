import random

list_of_diners = ["User1", "User2", "User3"]

picked = random.randint(0,2)

print(f"Bang!!! The person who pays for dinner is {list_of_diners[picked]}")

print("Option 2")

print(f"Bang!!! The person who pays for dinner is {random.choice(list_of_diners)}")