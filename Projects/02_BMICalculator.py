weight = int(input("What is your weight in kgs? : "))
height = int(input("What is your height in meters? : "))

BMI = float(round(weight / (height **2),1))
status =""

# BMI lower than 18.5 is under weight
# BMI between or equal to 18.5 and 24.9 is normal
# BMI above 24.9 is overweight

if BMI < 18.5:
    status ="UnderWeight"
elif 18.5 <= BMI <= 24.9:
    status ="Normal"
else:
    status ="Overweight"

print(f"Your BMI is : {BMI}. This value is {status}.")