#E_{n}(x)=(x+n)mod {26}
#D_{n}(x)=(x-n)\mod {26}
import random

alphabet = list([chr(i) for i in range(97, 123)])
upper_alphabet = ["M", "F","O", "B"]
#print(f"==>> upper_alphabet: {upper_alphabet}")


symbols = [
    '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '=', '+', '[', ']', '{', '}', '|', '\\',
    ':', ';', '"', "'", '<', '>', ',', '.', '?', '/',
    '`', '~'
]

numbers = ["0","1","2","3","4","5","6","7","8","9"]



def encrypt(e_word, modulation_userinput):
    global alphabet
    global symbols
    global numbers
    alphabet += symbols
    alphabet += upper_alphabet
    alphabet += numbers
    e_word = e_word.lower().replace("e", "3",).replace("i", "!").replace("o", "0").replace("l","7").replace("a", "@").replace("b", "8").replace("h", "4").replace("l","1").replace("g", "9").replace("'", "")
    
    #print(f"==>> alphabet: {alphabet}")
    encrypted_message=""
    encrypted_list = [alphabet.index(letter) for letter in e_word]
    encrypted_list.insert(random.randint(0, int(len(encrypted_list)))+1,random.randrange(int(26+int(len(symbols)) + int(len(numbers)) + int(len(upper_alphabet)))))
    #encrypted_list.insert(random.randrange(len(encrypted_list)),random.randint(-26, -1))
    for i in encrypted_list:
        i = (i - modulation_userinput) % (26 + int(len(symbols)) + int(len(numbers))+int(len(upper_alphabet)))
        encrypted_message += str(alphabet[i])
    print(f"Your encrypted message reads: {encrypted_message.replace("_"," ")}")

def dencrypt(de_word, modulation_userinput):
    global alphabet
    global symbols
    global numbers
    alphabet += symbols
    alphabet += upper_alphabet
    alphabet += numbers
    
    #print(f"==>> alphabet: {alphabet}")

    encrypted_message=""
    encrypted_list = [alphabet.index(letter) for letter in de_word.strip()]
    #print(f"==>> encrypted_list: {encrypted_list}")
    for i in encrypted_list:
        i = (i + modulation_userinput ) % (26 + int(len(symbols)) + int(len(numbers))+ int(len(upper_alphabet)))
        #print(f"{i}: {(i + modulation_userinput) % (26 + int(len(symbols)) + int(len(numbers))+ int(len(upper_alphabet)))}")
        encrypted_message += str(alphabet[i])
    print(f"Your dencrypted message reads: {encrypted_message.replace("_"," ").lower()}")

try:
    encrypt_decrypt = input("Would you like to Encrypt (E) or Decrypt(D): ").lower()
    if encrypt_decrypt == "e":
        print("OK: Encryption in Progress...")
    elif encrypt_decrypt =="d":
        print("OK: Decryption in Progress...")
    else:
        
        print(f"==>> encrypt_decrypt d: {encrypt_decrypt}")
        
        raise ValueError('Value Error: Please enter "E" or "D" when prompted: ')
    
    
    if encrypt_decrypt == "e":
        encrypted_word = input("Type the message would you like to encrypt: ").replace(" ","_")
        mod= int(input("What is your offset?: "))
    
        encrypt(encrypted_word, mod)
    else:
        dencrypted_word = input("Type the message would you like to dencrypt: ")
        mod= int(input("What is your offset?: "))

        dencrypt(dencrypted_word, mod)
    #print(alphabet)

except ValueError as e:
    print(f"Error: {e}")