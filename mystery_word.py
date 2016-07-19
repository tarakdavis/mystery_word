import random
import sys

def get_words():
    word_list = []
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            clean = line.strip('\n').lower()
            word_list.append(clean)
    return word_list

def easy_words(word_list):
    #easy_words = []
    return [word for word in word_list if len(word) >= 4 and len(word)<= 6]


def medium_words(word_list):
    #medium_words = []
    return [word for word in word_list if len(word) >= 6 and len(word) <= 8]

def hard_words(word_list):
    #hard_words = []
    return [word for word in word_list if len(word) >= 8 and len(word) <=50]

def random_word(word_list):
    return random.choice(word_list)

def display_word(word, bad_guesses, good_guesses):
    #print("secret word:", word)
    secret_word_list = list(word)
    for guess in bad_guesses:
       print(guess.upper(), end = ' ')
    print('')

    for guess in secret_word_list:
        if guess in good_guesses:
            print(guess.upper(), end = ' ')
        else:
            print('_', end = ' ')
               #display_word[index] = guess
               #for index, guess in enumerate(word_list):
    print("")

def has_chosen_valid_difficulty(difficulty):
    difficulty = difficulty.lower().strip()
    return difficulty in ['easy', 'medium', 'hard']

def has_guessed_word(word, good_guesses):
    for letter in word:
        if letter not in good_guesses:
            return False
    return True

def has_more_guesses(bad_guesses):
    return len(bad_guesses) < 7

def is_game_over(word, bad_guesses, good_guesses):
    return has_guessed_word(word, good_guesses) or not has_more_guesses(bad_guesses)

def main():
    word_list = get_words()
    bad_guesses = []
    good_guesses = []

    print("Welcome to the Mystery Word Game. Let's get started!")

    difficulty = ""

    while not has_chosen_valid_difficulty(difficulty):
        difficulty = input("Enter 'Easy', 'Medium', or 'Hard' OR 'Q' to Quit: ")
        if difficulty.lower() == 'q':
            sys.exit()
        elif difficulty.lower() == 'easy':
            word_list = easy_words(word_list)
        elif difficulty.lower() == 'medium':
            word_list = medium_words(word_list)
        elif difficulty.lower() == 'hard':
            word_list = hard_words(word_list)
        else:
            print("Your response was invalid. Try again.")

    word = random_word(word_list)

    while not is_game_over(word, bad_guesses, good_guesses):
        display_word(word, bad_guesses, good_guesses)

        print('Round: {}/7'.format(len(bad_guesses)))
        print('')
        print('')

        print("Your word has {} letters. Good luck!".format(int(len(word))))
        guess = input("Guess a letter: ")
        all_guesses = good_guesses + bad_guesses
        if not guess.isalpha():
            print("Invalid guess.")
            continue
        elif len(guess) != 1:
            print("Only one letter at a time.")
            continue
        elif guess in all_guesses:
            print("Oops! You already guessed that one.")
            continue
        elif guess in word:
            good_guesses.append(guess)
            print("Yes!")
        elif guess not in word:
            bad_guesses.append(guess)
            print("Nope.")
        else:
            break

    if has_guessed_word(word, good_guesses):
        print("Congratulations! You won!")
    else:
        if len(bad_guesses) == 7:
            print("You're out of guesses. Your word was {}.".format(word))
            print("You lost. Sorry, better luck next time.")

    play_again = input("Would you like to play again? Y/n: ")
    if play_again.lower() == 'n':
        print("Thanks for playing!")
        sys.exit()
    else:
        main()


if __name__ == '__main__':
    main()
