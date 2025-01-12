print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? :  "))
rider = False

if height > 120:
    print("You can ride the ride!")
    rider = True
else:
    print("Sorry, you have to grow taller!")