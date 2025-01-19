def add (n1, n2):
    return n1 + n2
def subtract (n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

calculator = {"+": add,
           "-": subtract,
           "*": multiply,
           "/": divide,
}

results_outer = 0
finished = ""

def calc (arg1, arg2):
    global results_outer
    for i in calculator:
        print(i)
    operation = input("What operation would you like to perform? ")
    if arg2 == False:
        n1 = arg1
    else:
        n1 = int(input("What is the first number? "))
    n2 = int(input("What is the second number? "))

    arg1 = calculator[operation](n1,n2)
    results_outer = arg1

    print(f" The results : {n1} {operation} {n2} = {arg1}")
    return results_outer


try:
    while not finished:
        calc(results_outer, finished)
        conitnue_prompt = input("Would you like to conitnue the operation? Yes (Y), No (N): ").lower()
        
        if conitnue_prompt == "y":
            finished = False
        else:
            finished = True
except ValueError as e:
    print(f"Error: {e}")