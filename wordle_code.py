from termcolor import colored

def correct(letter):
    return colored(letter, 'white', 'on_green', attrs=['bold'])
def present(letter):
    return colored(letter, 'white', 'on_yellow', attrs=['bold'])
def absent(letter):
    return colored(letter, 'white', 'on_grey', attrs=['bold'])

# this is an example for printing coloured letters
# print(correct("h") + present("ell") + absent("o"))

# the secret is hard-coded here
secret = "wedge"

# your code below

# Create a function to ask for an input of a 5 letter word, prompt user again if the word is not 5 characters

def valid_guess():
    guess = input("Input your guess: ")
    while len(guess) != 5:
        print("Guess must be a 5 letter word")
        guess = input("Input your guess: ")
    return guess
guess = valid_guess()


while True:
    # Generate a hint list which will show for each character in guess if they are correct, present or absent
    hint = [None]*len(guess)
    # Generate an empty list which if a letter is correct or present in the secret word it will be added to 
    letters_used = []

    # For each character in guess, check if it is in the correct position
    for char in range(len(guess)):
        if guess[char] == secret[char]:
            hint[char]="correct"
            letters_used.append(guess[char])
    # For each character in guess loop to determine if it is present or absent
    for char in range(len(guess)):
    # Check if the letter appears more times in the secret word than how many times the letter has been assigned a value
    # Also check if the letter has already been assigned as correct (if so skip the letter)
        if secret.count(guess[char]) > letters_used.count(guess[char]) and not hint[char] == "correct":
    # Check if the character is within the word
            if guess[char] in secret:
                hint[char]="present"
                letters_used.append(guess[char])
    # If the character is not within the word and hasn't been assigned as correct then assign it as absent
        elif not hint[char] == "correct":
            hint[char]="absent"

    # Construct the visual hint from the hint list
    visual = ''
    # By indexing the hint list we can append the corresponding item from the guess and colout it as per the 'status'
    for i in range(len(hint)):
        if hint[i] == 'correct':
            visual += correct(guess[i])
        elif hint[i] == 'present':
            visual += present(guess[i])
        else:
            visual += absent(guess[i])
    print(visual)
    # If there is the same correct statuses as number of letters then a congratulatory message will be printed and the code will break
    if hint.count('correct')==len(guess):
        print("Well done!")
        break
    
    # Prompt the user to enter another guess if needed
    guess = valid_guess()


            

