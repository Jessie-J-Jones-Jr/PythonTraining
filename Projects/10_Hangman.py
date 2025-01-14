from wonderwords import RandomWord
word_create = RandomWord()
word_list = []
word_length = int(input("How many letters in the word you want to guess?  "))
display_dashes = ""
word_vault = []

for i in range(1):
    new_word = word_create.word(word_min_length=word_length, word_max_length=word_length)
    word_list = list(new_word)
    # print(f"==> word_list {word_list}")
    # print("Word "+str(i+1)+" : ", new_word)

for i in range(word_length):
    display_dashes += " _ "

for i in range(word_length):
    word_vault.append(" _ ")

print(f"==>> display_dashes: {display_dashes}")

# print(f"==>> word_vault: {word_vault}")

guessed_letter = input("Guess your first letter: ")

for i in range(word_length):
    if guessed_letter == word_list[i]:
        # print("RIGHT")
        word_vault[i] = guessed_letter
        
    # else:
        # print("WRONG")
# print(f"==>> word_vault: {word_vault}")

display_dashes =""
for i in range(word_length):
    display_dashes += " " + word_vault[i] +" "
    
print(f"==>> display_dashes: {display_dashes}")

#break up into functions
# add a while loop and game status variables if the game is still in progress keep allowing for guess
#with a break out for if the wrong guess counter is exhausted game over
# neutral check function for if the users guesses the same letter that was already guessed.
# the finally get graphics

#https://www.askpython.com/python-modules/wonderwords-module