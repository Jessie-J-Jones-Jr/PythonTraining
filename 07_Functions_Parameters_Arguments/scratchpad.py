def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 ==0 and year % 400 == 0:
            print(True)
        else:
            print(False)
    # Don't change the function name.

is_leap_year(2004)


# age=int(input("How old are you in years?: "))


# def results ():
#     global age
#     if age >90:
#         print("You are in the Bonus years of your life!!! Enjoy!!")
#     else:
#         results = (90*52) - (age*52)
#         print(f"You have {results} weeks left.")

# results()



# def true_love_number(first_person,
#                      second_person,
#                      first_name1,
#                      first_name2,
#                      last_name
# ):
#     t = first_person.count("t") + second_person.count("t")
#     r = first_person.count("r") + second_person.count("r")
#     u = first_person.count("u") + second_person.count("u")
#     e_1 = first_person.count("e") + second_person.count("e")
#     l = first_person.count("l") + second_person.count("l")
#     o = first_person.count("o") + second_person.count("o")
#     v = first_person.count("v") + second_person.count("v")
#     e_2 = e_1


#     total_1 = sum([t,r,u,e_1])
#     total_2 = sum([l,o,v,e_2])

#     print(f"{first_name1.capitalize()} and {first_name2.capitalize()} Your combined love scrore is {total_1}{total_2}!!")
#     # print(first_person)
#     # print(second_person)
#     love_value = int(str(total_1) + str(total_2))
#     if love_value > 60:
#         print(f"Congratulations Mr. and Mrs. {last_name}. You are True Lovers!!! ")
#     else:
#         print(f"Dump each other...find another love :(")

# try:
#     name_1 = (input("What is your First and Last Name?: "))
#     first_name1 = name_1.split(" ")[0]
#     mod_name_1 = name_1.replace( " ","").lower().strip()
#     last_name = name_1.split(" ")[-1]
    
#     if not mod_name_1.isalpha():
#         raise ValueError("Name should only contain letters and should not be empty")
    
    
#     name_2 = (input("What is the First and Last Name of your true love?: "))
#     first_name2 = name_2.split(" ")[0]
#     mod_name_2 = name_2.replace( " ","").lower().strip()
#     if not mod_name_2.isalpha():
#         raise ValueError("Name should only contain letters and should not be empty")
    
#     true_love_number(first_person=mod_name_1,
#                      second_person=mod_name_2,
#                      first_name1=first_name1,
#                      first_name2=first_name2,
#                      last_name=last_name
#     )

# except ValueError as e:
#     print(f"Error: {e}")