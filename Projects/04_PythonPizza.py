print("Welcome to Python Pizza Deliveries!!\n#################################\n")

size = input("What size Pizza would you like? Small (S), Medium (M), or Large (L)? : ").lower()
pepperoni = input("Would you like to add Pepperoni with your Pizza? Yes (Y) or No (N)? : ").lower()
extra_cheese = input("What you like to add extra Cheese with your Pizza? Yes (Y) or No (N) :").lower()
bill = 0

if size == "l":
    bill += 25
elif size == "m":
    bill += 20
else:
    bill +=15

if size =="s" or "m":
    if pepperoni == "y":
        bill += 3
else:
    if pepperoni =="y":
        bill += 2

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}! : ")