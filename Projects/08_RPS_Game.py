import random

# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]
results = ["",""]
user_choise = input("Choose Rock (R), Paper (P) or Scissors (S): ").lower()
winner = ""

if user_choise == "r":
    user_choice = rock
    results[0] = "r"
elif user_choise == "p":
    user_choice = paper
    results[0] = "p"
else:
    user_choice = scissors
    results[0] = "s"
        
computer_choice = random.choice(options)
if computer_choice == rock:
    results[1] = "r"
elif computer_choice == paper:
 
    results[1] = "p"
else:
    computer_choice = scissors
    results[1] = "s"

if results[0] == results[1]:
    winner = "The Game is a Tie!! No one wins!!"
elif results[0] == "r" and results[1] == "s":
    winner = "User Wins!!"
elif results[0] == "r" and results[1] == "p":
    winner = "Computer Wins!!"
elif results[0] == "s" and results[1] == "r":
    winner = "Computer Wins!!"
elif results[0] == "s" and results[1] == "p":
    winner = "User Wins!!"
elif results[0] == "p" and results[1] == "r":
    winner = "User Wins!!"
else:
    winner = "Computer Wins!!"

print(f"\nThe Computer chose:\n{computer_choice}")
print(f"You chose:\n {user_choice}")
print("################################################################")
print(winner)