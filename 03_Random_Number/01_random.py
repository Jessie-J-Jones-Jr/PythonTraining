import random
import testmodule

number =random.randint(1,10000)

print(number)

number = number * testmodule.number3

print(float(number))

number_new = random.random()*10
print(f"number_new is {number_new}")

#docs.python.org/3/library/random.html