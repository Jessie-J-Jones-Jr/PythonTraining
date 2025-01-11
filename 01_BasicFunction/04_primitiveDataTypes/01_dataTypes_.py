#Pulling out characters from a string#

print("Hello")

print("The length of Hello is.." + str(len("Hello")))

#Subscripting is using [] to pull a specifc location from a data type
#Starting from index number 0 #
print ("\nSubscripting")
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

#Negative Index values work as well
print ("\nSubscripting with Negative Index ################")
print("Hello"[-1])
print("Hello"[-2])
print("Hello"[-3])
print("Hello"[-4])
print("Hello"[0])

print ("\nInteger or String ################")
print ("123" + "456")
#Versus
print (123 + 456)

#Using commas means the input are separate arguments 
# Since the print function has no other positional parameters
# It treats it as a separate operation which is good for
# printing multiple variables#

print("\n######Simple Example############")
print(123,456)


print("\n######Complex Example Example############")
a = 5
b = 10
c = a * b
d = c - 15
e = d / 5

# Print all variables at once
print("Debugging:", "a =", a, "b =", b, "c =", c, "d =", d, "e =", e)