#Variables needed

#Bill as input
bill = input("What is the amount of the bill?\n")

#Convert to integer

bill = float(bill)

#What is the percentage you want to give as a tip?

tip_percentage = input("How much do you want to tip? ex 10%, 20%, 30%?\n")

#Convert to integer

tip_percentage = float(tip_percentage)

tip_amount = bill * (tip_percentage/100)

#How many people are splitting the bill?
total_bill = round(bill + tip_amount)

print(f"The correct amount of tip to leave is ${round( tip_amount,2)}. This means the total bill is ${total_bill}.")

num_people_eating = int(input("How many people are splitting the bill?\n"))

print(f"That means the final bill will be ${round(total_bill / num_people_eating,2)}")


#Analysis 
# Could make it better by handdling the $ and % if inputting by the User 
# Will redo once if statements are covered#
