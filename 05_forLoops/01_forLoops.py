fruits = ["Apple", "Pear", "Peach"]



for newname in fruits:
    print(newname)
    print(newname + " pie")
print(f"==>> fruits: {fruits}")

scores = [15, 20, 160, 33, 161, 88]

sum_scores = sum(scores)
print(f"==>> sum_scores: {sum_scores}")

sum_manual = 0
for sum in scores:
    sum_manual += sum
    print(f"==>> sum_manual: {sum_manual}")
print(f"==>> sum_manual: {sum_manual}")

max_manual = 0
max_number = max(scores)
print(f"==>> max_number: {max_number}")

for maxnum in scores:
    if maxnum > max_manual:
        max_manual = maxnum
        print(f"==>> max_manual: {max_manual}")
print(f"==>> max_manual: {max_manual}")

