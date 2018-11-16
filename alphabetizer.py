"""
Alphabetize the words in any .txt file
"""
def alphabetize(words, pattern, split_lines=False):
    '''
    Returns a list of each capitalized word in alphabetical order
    '''
    if not split_lines:
        return sorted(list(map(lambda x: x.capitalize(), words.split(pattern))))
    else:
        return sorted(list(map(lambda x: x.capitalize(), words.splitlines())))

def join_words(words):
    '''
    Joins list of words together separated by a comma and a space
    '''
    return ', '.join(words)

try:
    # Ask the user for the name of the file they wish to alphabetize
    file_name = input('Name of text file with words that you wish to alphabetize. (Ex: words.txt) \n')

    # Try to open the file
    file = open(file_name, 'r')

    # Get the contents of the file
    file_contents = file.read()

    # Close the file
    file.close()

except FileNotFoundError:
    # Handles the error of not being able to access the desired file
    print('I\'m sorry! I could not find that file. Try creating it, or navigating into a different directory.')

else:
    # Continue with the program
    # Ask the user what characters separate each of the words in the text file
    pattern = input('Pattern/Characters that separates each word in the text file. (Default is comma followed by a space. If new line, type "new line".) \n')
    split_on_lines = False

    # Check if nothing was input
    if pattern == '':
        pattern = ', '
    elif pattern == 'new line':
        split_on_lines = True

    # Create the string to write to either rewrite the text file, or create a new one
    alphabetized_words = join_words(alphabetize(file_contents, pattern, split_on_lines))
    
    # Ask the user if they wish to override existing file or create a new one.
    while 1:
        try:
            alphabetize_file = input('Would you like to rewrite existing file, or create a new one? (r/rewrite or n/new) \n')

            # If the user didn't provide the desired input, raise a RuntimeError
            if not alphabetize_file in ['n', 'r', 'rewrite', 'new']:
                raise RuntimeError

        except RuntimeError:
        	# Provide an error message, and ask again
            print('I\'m sorry! Please tell me if you wish to rewrite or create a new file. \n')
            continue

        else:
            # Continue with the program
            break

    # If the user wants to create a new file, do so
    if alphabetize_file in ['n', 'new']:
        # Ask for the new file's name
        new_file_name = input('Name of new file. ')

        # Create and open the file
        new_file = open(new_file_name, 'w+')

        # Write to the new file
        new_file.write(f'Alphabetized words:\n {alphabetized_words}')

        # Close the new file
        new_file.close()

    else:
        # Open the file
        file = open(file_name, 'w+')

        # Rewrite the file
        file.write(f'Alphabetized words:\n {alphabetized_words}')

        # Close the file
        file.close()
