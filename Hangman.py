import os
import time


# This function prints the welcome screen and gets the users word's file and index
def welcome():
    global file_path, index, MAX_TRIES
    HANGMAN_ASCII_ART = """  _    _
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |
                     |___/"""
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART, '\n', MAX_TRIES)
    file_path = 'words.txt' # input("Enter words' file path: ")
    index = input("Enter index: ")
    print("Let's Play!")


old_letters_guessed = []

num_of_tries = 0


# This function use the user's chosen index from the word's file and returns a secret word
def choose_word(file_path, index):
    global secret_word, hidden_word
    f = open(file_path, 'r')
    words_list = f.read().split()
    if int(index) not in range(len(words_list)):
        print("Please choose index in range 1 -", len(words_list))
        index_1 = input("Enter index: ")
        secret_word = words_list[int(index_1)-1]
    else:
        secret_word = words_list[int(index)-1]
    return secret_word


# This function gets a letter from the user and check if it's a single alphabetic letter and if it's already guessed
def try_update_letter_guessed(old_letters_guessed):
    global letter_guessed, num_of_tries
    letter_guessed = input("Please guess a letter: ")
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed.lower() in old_letters_guessed:
        print("X")
        print(" -> ".join(old_letters_guessed))
    else:
        old_letters_guessed.append(letter_guessed)
        if letter_guessed not in secret_word:
            print(":(")
            num_of_tries += 1
            print_hangman(num_of_tries)


# This function checks if the user's guessed letter is valid or not
def check_valid_input(letter_guessed, old_letters_guessed):
    if letter_guessed.isalpha() and old_letters_guessed.count(letter_guessed) <= 1:
        return True
    else:
        return False


# This function prints the 'Hangman's' photo according to the number of tries
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {'try_1': """x-------x""", 'try_2': """
    x-------x
    |
    |
    |
    |
    |""", 'try_3': """
    x-------x
    |       |
    |       0
    |
    |
    |""", 'try_4': """
    x-------x
    |       |
    |       0
    |       |
    |
    |""", 'try_5': """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 'try_6': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 'try_7': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
    for key in HANGMAN_PHOTOS.keys():
        if int(key[-1])-1 == num_of_tries:
            print(HANGMAN_PHOTOS.get(key))


# This function shows the missing and the correct letters of the secret word
def show_hidden_word(secret_word, old_letters_guessed):
    global hidden_word
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter
        else:
            hidden_word += "_ "
    return hidden_word


# This function checks if the user succeeded guessing the secret word and prints if win or lose
def check_win(secret_word):
    global hidden_word, i, MAX_TRIES
    i = 0
    if hidden_word == secret_word:
        print("WIN")
        i = 1
    if num_of_tries == MAX_TRIES:
        i = 1
        print("LOSE")


# This function clears the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# This function is reloading the game or exit according to the user input
def reload_game():
    global old_letters_guessed, num_of_tries
    answer = input("Would you like to play again? y/n: ")
    if answer == "y":
        time.sleep(1)
        clear_screen()
        num_of_tries = 0
        old_letters_guessed = []
        load_game()
    else:
        print("Thanks for playing, bye bye!")
        time.sleep(2)
        clear_screen()


# This function runs all the functions into one flowing game
def load_game():
    welcome()
    choose_word(file_path, index)
    print_hangman(num_of_tries)
    print(len(secret_word) * '_ ')
    while show_hidden_word(secret_word, old_letters_guessed) != secret_word:
        try_update_letter_guessed(old_letters_guessed)
        print(show_hidden_word(secret_word, old_letters_guessed))
        check_win(secret_word)
        if i == 1:
            break
    reload_game()


if __name__ == '__main__':
    load_game()
