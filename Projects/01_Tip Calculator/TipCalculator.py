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


print( "The correct amount of tip to leave is $" + str( round( tip_amount,2)) )


#Analysis 
# Could make it better by handdling the $ and % if inputting by the User 
# Will redo once if statements are covered#