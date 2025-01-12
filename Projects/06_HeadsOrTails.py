import random

heads_or_tails = ""

flip_result = round(random.random()*1,0)

if flip_result == 0:
    heads_or_tails = "heads"
else:
    heads_or_tails = "tails"

print(f"The result of the flip is {heads_or_tails}.")