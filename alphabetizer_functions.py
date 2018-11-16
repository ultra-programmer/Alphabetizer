"""
Define the functions outside of the main program
so the functions can be imported and reused
"""
def alphabetize(words, pattern, split_lines=False):
    '''
    Returns a list of each capitalized word in alphabetical order
    '''
    if not split_lines:
        return list(filter(bool, sorted(map(lambda x: x.capitalize(), words.split(pattern)))))
    else:
        return list(filter(bool, sorted(map(lambda x: x.capitalize(), words.splitlines()))))

def join_words(words):
    '''
    Joins list of words together separated by a comma and a space
    '''
    return ', '.join(words)