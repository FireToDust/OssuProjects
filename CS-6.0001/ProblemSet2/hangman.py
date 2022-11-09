# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import time

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def make_delayed_print(delay=0.0, ):
    def inner(*args, end="\n"):
        for i in " ".join(args):
            print(i, end="", flush=False)
            time.sleep(delay)
        print(end, end="", flush=False)

    return inner


def loser():
    print("""
     __     __           _                    
     \\ \\   / /          | |                   
      \\ \\_/ /__  _   _  | |     ___  ___  ___ 
       \\   / _ \\| | | | | |    / _ \\/ __|/ _ \\
        | | (_) | |_| | | |___| (_) \\__ \\  __/
        |_|\\___/ \\__,_| |______\\___/|___/\\___|

                                              """)


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    for i in secret_word:
        if not i in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    result = ""
    for i in secret_word:
        if i in letters_guessed:
            result += i + " "
        else:
            result += "_ "
    return result


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    return "".join([x for x in string.ascii_lowercase if x not in letters_guessed])

def get_score(secret_word, guesses_remaining):
    
    return guesses_remaining * len(set(secret_word))

def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """
    delayed_print = make_delayed_print(0.2)
    fast_delayed_print = make_delayed_print(0.05)

    # delayed_print = print
    # fast_delayed_print = print

    guesses_remaining = 6
    letters_guessed = ""

    delayed_print("Welcome to hangman!!!!", end="")
    fast_delayed_print("(WAHAHAHAHAHAHA)")
    time.sleep(1)
    fast_delayed_print("Im thinking of a word with length", str(len(secret_word)))
    fast_delayed_print("You have " + str(guesses_remaining) + " guesses to guess the letters of the word, guesses dont count if "
                                                    "you guess right.")

    while guesses_remaining > 0:
        fast_delayed_print("Current word: " + get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed):

            fast_delayed_print("You guessed the word in time !!!! (IM SAD  ):< )")
            fast_delayed_print("Your score was " + str(get_score(secret_word, guesses_remaining)))

            return True

        available_letters = get_available_letters(letters_guessed)

        fast_delayed_print("You have " + str(guesses_remaining) + " guesses left!")
        fast_delayed_print("Available letters: " + available_letters)

        guess = input("Guess: ")[0].lower()
        if guess not in available_letters:
            fast_delayed_print("You have already guessed that.")
        elif guess in secret_word:
            letters_guessed += guess
            fast_delayed_print("Correct!")
        else:
            letters_guessed += guess
            guesses_remaining -= 1
            fast_delayed_print("WRONG!!! hehe")


    fast_delayed_print("The word was " + secret_word)
    loser()
    return False


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
