#def functionName(arg, arg2, arg3):
    #print("Hello World")

#functionName()
#Error TypeError: functionName() missing 3 required positional arguments: 
# 'arg', 'arg2', and 'arg3'   

test1 = "MMM"
test2 = "JJJ"
test3 = "KKK"

def functionName(arg, arg2, arg3):
    print("Hello World " + arg + arg2 + arg3)

functionName(test1, test2, test3)

#Output Hello World MMMJJJKKK
