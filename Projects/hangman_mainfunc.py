def main_game():
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
    #print(f"==>> word_vault[i]: {word_vault}")