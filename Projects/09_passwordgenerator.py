import string
import random

# English letters
letters = list(string.ascii_uppercase + string.ascii_lowercase)

# Spanish letters
spanish_letters = ['Á', 'É', 'Í', 'Ó', 'Ú', 'Ñ', 'á', 'é', 'í', 'ó', 'ú', 'ñ']

# German letters
german_letters = ['Ä', 'Ö', 'Ü', 'ß', 'ä', 'ö', 'ü']

# Combine all letters
extended_letters = letters + spanish_letters + german_letters
# print(f"==>> extended_letters: {extended_letters}")
numbers = list(range(1, 101))
# print(f"==>> numbers: {numbers}")
symbols = list(string.punctuation)
# print(f"==>> symbols: {symbols}")

user_letters = int(input("How many letters do you want in your password?\n"))
user_numbers = int(input("How many numbers do you want in your password?\n"))
user_symbols = int(input("How many symbols do you want in your password?\n"))

password = []


for password_letters in range(0, user_letters):
    password.append(random.choice(extended_letters))
for password_numbers in range(0, user_numbers):
    password.append(random.choice(numbers))
for password_symbols in range(0, user_symbols):
    password.append(random.choice(symbols))
    
print(f"==>> password: {password}")
random.shuffle(password)
print(f"==>> password: {password}")

new_password = ""
for char in password:
    new_password = str(new_password) + str(char)

print(f"Your new password is: {new_password}")