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


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    secret_word_list = list(secret_word)

    for letter in range(len(secret_word_list)):
        if secret_word_list[letter] not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    secret_word_list = list(secret_word)
    guessed_word_list = list(range(len(secret_word_list)))

    for letter in range(len(secret_word_list)):
        if secret_word_list[letter] in letters_guessed:
            guessed_word_list[letter] = secret_word_list[letter]
        else:
            guessed_word_list[letter] = "_ "
    
    guessed_word = ''.join([str(i) for i in guessed_word_list])

    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    available_letters = "abcdefghijklmnopqrstuvwxyz"

    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, "")

    return available_letters

def is_vowel(letter):
    '''
    letter: string of 1 character
    '''

    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter not in vowels:
        return False
    else:
        return True

def is_input_valid(letter):
    '''
    letter: string of 1 character
    '''
    
    available_letters = list("abcdefghijklmnopqrstuwvxyz*")

    if letter not in available_letters:
        return False
    
    return True

def hangman(secret_word):
    '''
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
    '''

    secret_word_size = len(secret_word)
    secret_word_uniq = len(set(secret_word))
    letters_guessed = list("")
    letter_guessed = ""
    total_score = 0
    warnings = 3
    guesses = 6
    guess = ""

    print("Welcome to the game of Hangman!")
    print("I am thinking of a word that is %d letters long" % (secret_word_size))

    while guesses >= 0:

        print("-----------------------")

        if guesses == 0:
            print("Sorry, you ran out of guesses.")
            print("The word was ", secret_word)
            break

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses * secret_word_uniq

            print("Congratulations! you won!")
            print("Your total score for this game is: ", total_score)
            break

        available_letters = get_available_letters(letters_guessed)
        
        print("You have %d guesses left" % (guesses))
        print("Available letters: ", (available_letters))
        
        letter_guessed = input("Please guess a letter: ")

        if not is_input_valid(letter_guessed):
            if warnings == 0:
                warnings = 3
                guesses -= 1
                print("You lost one guess because of too many invalid letters!")

            warnings -= 1
            print("Oops! That is not a valid letter. You now have %d warnings left" % (warnings))
            letter_guessed = ""
        elif letter_guessed in letters_guessed:
            if warnings == 0:
                warnings = 3
                guesses -= 1
                print("You lost one guess because of too many invalid letters!")
            
            warnings -= 1
            print("Oops! You've already guessed this letter. You now have %d warnings left" % (warnings))


        letters_guessed.append(letter_guessed)

        if letter_guessed not in secret_word:
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            
            if is_vowel(letter_guessed):
                guesses -= 2
            else:
                guesses -= 1
        else:
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
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

    split_word = my_word.replace("_ ", " ")

    if len(split_word) == len(other_word):
        for l in range(len(split_word)):
            if split_word[l] != other_word[l] and split_word[l] != " ":
                return False
    else:
        return False

    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    possible_matches = []
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)

    if len(possible_matches) == 0:
        print("No matches found")
        return None

    print(possible_matches)


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
    
    secret_word_size = len(secret_word)
    secret_word_uniq = len(set(secret_word))
    letters_guessed = list("")
    letter_guessed = ""
    total_score = 0
    warnings = 3
    guesses = 6
    guess = ""

    print("Welcome to the game of Hangman!")
    print("I am thinking of a word that is %d letters long" % (secret_word_size))

    while guesses >= 0:

        print("-----------------------")

        if guesses == 0:
            print("Sorry, you ran out of guesses.")
            print("The word was ", secret_word)
            break

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses * secret_word_uniq

            print("Congratulations! you won!")
            print("Your total score for this game is: ", total_score)
            break

        available_letters = get_available_letters(letters_guessed)
        
        print("You have %d guesses left" % (guesses))
        print("Available letters: ", (available_letters))
        
        letter_guessed = input("Please guess a letter: ")

        if not is_input_valid(letter_guessed):
            if warnings == 0:
                warnings = 3
                guesses -= 1
                print("You lost one guess because of too many invalid letters!")

            warnings -= 1
            print("Oops! That is not a valid letter. You now have %d warnings left" % (warnings))
            letter_guessed = ""
        elif letter_guessed in letters_guessed:
            if warnings == 0:
                warnings = 3
                guesses -= 1
                print("You lost one guess because of too many invalid letters!")
            
            warnings -= 1
            print("Oops! You've already guessed this letter. You now have %d warnings left" % (warnings))


        letters_guessed.append(letter_guessed)

        if letter_guessed not in secret_word and letter_guessed != "*":
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
    
            if is_vowel(letter_guessed):
                guesses -= 2
            else:
                guesses -= 1
        elif letter_guessed == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
