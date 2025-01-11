#################################
#Good Code
#user = "me"
#print(user)


#################################
#Syntax Error
#user name ="me"
#print(user name)


#################################
#Good Python Syntax
#user_name ="me"
#print(user_name)


#################################
#Bad practice

#u = "Jack"
#l = len (u)
#print(u)

#you won't remember these variables later if you have to modify code

#################################
#Name Error

#user ="Jack"
#print(username)
#Debug the code

#################################
#bad practice using function names as variable names
#input = "Jack"
#print(input)
#input("what is your name?")
# TypeError: 'str' object is not callable. Essentially you have the erased the input function (only for this run)
# with a string and now when you try to run it as a function it throws an error 
# the will change as per the variable type ex input = 5 would through a "int" object is not callable 
# For this reason you should not use a python function name as a variable.