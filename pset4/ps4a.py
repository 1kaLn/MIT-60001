# Problem Set 4A
# Name: Guilherme Kalani
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return list(sequence)
    
    perms = []
    
    for char in sequence:
        for perm in get_permutations(sequence.replace(char, '', 1)):
            perms.append(char+perm)

    return perms
    

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    first_input = 'abc'
    second_input = 'cat'
    third_input = 'ufo'

    first_output = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    second_output = ['cat', 'cta', 'act', 'atc', 'tca', 'tac']
    third_output = ['ufo', 'uof', 'fuo', 'fou', 'ouf', 'ofu']

    print('Input: ', first_input)
    print('Expected Output: ', first_output)
    print('Actual Output: ', get_permutations(first_input))

    print('Input: ', second_input)
    print('Expected Output: ', second_output)
    print('Actual Output: ', get_permutations(second_input))

    print('Input: ', third_input)
    print('Expected Output: ', third_output)
    print('Actual Output: ', get_permutations(third_input))
