import random
from wonderwords import RandomWord
word_create = RandomWord()
import hangman_status
import hangman_title
#from hangman_mainfunc import main_game


title = hangman_title.hangman_title_graphix
game_progress = hangman_status.hang_man_status
word_length = int(random.randint(5, 17))
word_list = []
display_dashes = ""
word_vault = []
guessed_vault = []
guessed_wrong_vault = []
revealed_word = ""
new_word = ""
strikes = 0
game_over = False
quit = False

def reset():
    global word_list
    word_list = []
    global display_dashes
    display_dashes = ""
    global word_vault
    word_vault = []
    global guessed_vault
    guessed_vault = []
    global guessed_wrong_vault 
    guessed_wrong_vault = []
    global revealed_word 
    revealed_word = ""
    global new_word
    new_word = ""
    global strikes
    strikes = 0
    global game_over
    game_over = False
    global quit
    quit = False
    print(title)

reset()

def word_creation():
    global new_word
    global word_list
    global display_dashes
    global strikes
    global revealed_word

    for i in range(1):
        new_word = word_create.word(word_min_length=word_length, word_max_length=word_length)
        word_list = list(new_word)
        revealed_word = new_word
        #print(f"==> word_list {word_list}")
        #print("Word "+str(i+1)+" : ", new_word)

    for i in range(word_length):
        display_dashes += " _ "

    for i in range(word_length):
        word_vault.append(" _ ")
    print(game_progress[strikes])
    print(display_dashes)

# print(f"==>> word_vault: {word_vault}")

word_creation()



def main_game():
    global game_over
    global strikes
    global display_dashes
    global game_over

    while not game_over:
    
        guessed_letter = input("Guess your first letter: ").lower()

        if guessed_letter in guessed_vault:
                print(f"You already guessed: {guessed_letter.upper()}. Please try again.")
        else:
            guessed_vault.append(guessed_letter)
            if guessed_letter not in new_word:
                strikes += 1
                print(f"\n\n\n################### {strikes}/6 STRIKES ####################")
                
            else:
                for i in range(word_length):
                    if guessed_letter == word_list[i]:
                        word_vault[i] = " " + guessed_letter.upper() + " "

            if guessed_letter not in revealed_word:
                    guessed_wrong_vault.append(guessed_letter.upper())

            if strikes == 6:
                print(f"#################### GAME OVER #####################")
                game_over = True
                print(game_progress[strikes])
                print(f"The Hanging Man's last word was.....{revealed_word.upper()}.")
                # print(f"==>> word_vault: {word_vault}")

            display_dashes = ''.join(word_vault)

            if not game_over:
                print(game_progress[strikes])
                print(f"These letters are not in the word: {guessed_wrong_vault}")
                print(display_dashes)
                
            if display_dashes.replace(" ","").lower() == revealed_word:
                #print(f"==>> display_dashes.replace(" ",""): {display_dashes.replace(" ","")}")
                game_over=True
                print ("\n########################### YOU WON!!!!!!!!!! ###########################\n")
                print(title)
    restart_prompt = input("Would you like to try again? Yes(Y) or No (N)?: ").lower()

    if restart_prompt=="y":
        reset()
        word_creation()
        main_game()
    else:
        quit = True
        print("Goodbye")
    #print(f"==>> word_vault[i]: {word_vault}")

main_game()


    #print(f"==>> display_dashes: {display_dashes}")


#https://www.askpython.com/python-modules/wonderwords-module