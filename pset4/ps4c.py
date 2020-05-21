# Problem Set 4C
# Name: Guilherme Kalani
# Collaborators:
# Time Spent: x:xx

import string, random
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        
        return self.message_text
            
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        
        valid_words_copy = self.valid_words.copy()

        return valid_words_copy

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        letters_mapping_lower = dict((key, key) for key in string.ascii_lowercase)
        vowels_mapping = dict((key, key) for key in VOWELS_LOWER)
        vowels_perm_list = list(vowels_permutation.lower())
        
        index = 0
        for letter in vowels_mapping.keys():
            vowels_mapping.update({ letter: vowels_perm_list[index] })
            index += 1

        for letter in vowels_mapping.keys():
            letters_mapping_lower.update({ letter: vowels_mapping.get(letter) })

        letters_mapping_upper = dict((k.upper(), v.upper()) for k, v in letters_mapping_lower.items() )
             
        return { **letters_mapping_upper, **letters_mapping_lower }
            
         
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
       
        mapped_message = list(self.message_text)

        for letter in range(len(mapped_message)):
            if mapped_message[letter] in transpose_dict:
                mapped_message[letter] = transpose_dict.get(mapped_message[letter])

        return "".join(mapped_message)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''

        og_message_text = self.message_text
        perms = get_permutations(VOWELS_LOWER)
        perm_word_counter = dict((k, 0) for k in perms)

        for perm in perms:
            mapped_dict = self.build_transpose_dict(perm)
            self.message_text = self.apply_transpose(mapped_dict)
            message_split = self.message_text.split(' ')
            for word in message_split:
                if is_word(self.valid_words, word):
                    perm_word_counter[perm] = perm_word_counter.get(perm, 0) + 1

            self.message_text = og_message_text

        best_perm = max(perm_word_counter, key=perm_word_counter.get)
        best_map = self.build_transpose_dict(best_perm)

        return self.apply_transpose(best_map)

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    
    message_two = SubMessage("How are you?")
    permutation_two = "iuoae"
    enc_dict_two = message_two.build_transpose_dict(permutation_two)
    enc_message_two = EncryptedSubMessage(message_two.apply_transpose(enc_dict_two))
    print("Original message:", message_two.get_message_text(), "Permutation:", permutation_two)
    print("Expected encryption:", "Haw iru yae?")
    print("Actual encryption:", message_two.apply_transpose(enc_dict_two))
    print("Decrypted message:", enc_message_two.decrypt_message())

    message_three = SubMessage("How old are you, friend?")
    permutation_three = "oaeui"
    enc_dict_three = message_three.build_transpose_dict(permutation_three)
    enc_message_three = EncryptedSubMessage(message_three.apply_transpose(enc_dict_three))
    print("Original message:", message_three.get_message_text(), "Permutation:", permutation_three)
    print("Expected encryption:", "Huw uld ora yui, freand?")
    print("Actual encryption:", message_three.apply_transpose(enc_dict_three))
    print("Decrypted message:", enc_message_three.decrypt_message())
