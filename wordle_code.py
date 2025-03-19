from termcolor import colored
import random
import colorama
import time

# Enable ANSI colours on Windows
colorama.init()

def correct(letter):
    return colored(letter, 'white', 'on_green', attrs=['bold'])
def present(letter):
    return colored(letter, 'white', 'on_yellow', attrs=['bold'])
def absent(letter):
    return colored(letter, 'white', 'on_grey', attrs=['bold'])

# this is an example for printing coloured letters
# print(correct("h") + present("ell") + absent("o"))

# Word list generated by ChatGPT to pick a random word from
word_list = [
    "apple", "baker", "candy", "delta", "eagle", "fable", "grape", "happy", "ideal", "joker",
    "koala", "lemon", "mango", "noble", "ocean", "piano", "quilt", "raven", "sunny", "tiger",
    "umbra", "vivid", "whale", "xenon", "youth", "zebra", "abide", "blaze", "charm", "drift",
    "ember", "flute", "glide", "haste", "image", "jolly", "knack", "latch", "mirth", "novel",
    "optic", "pride", "quark", "rover", "sight", "tempo", "urban", "vigor", "witty", "xylol",
    "yacht", "zephyr", "adobe", "binge", "cloud", "daisy", "elbow", "frost", "glint", "hound",
    "ivory", "jumbo", "karma", "lunar", "moody", "nylon", "oasis", "pluck", "quill", "rider",
    "sable", "torus", "usher", "vixen", "woven", "xerox", "yodel", "zesty", "amber", "basil",
    "cider", "dingo", "eclat", "fancy", "gloom", "hatch", "icily", "jewel", "kinky", "logic",
    "motto", "nifty", "omega", "pesto", "quirk", "risky", "syrup", "tango", "ultra", "vowel",
    "whisk", "xenia", "yield", "zonal", "acorn", "blink", "crisp", "dwell", "epoch", "flick",
    "grasp", "hover", "inbox", "judge", "kayak", "lapse", "mirth", "nexus", "octet", "plush",
    "quota", "realm", "shiny", "twist", "unite", "verge", "wrist", "xenon", "yummy", "zebra",
    "aglow", "bison", "crane", "deter", "elude", "fudge", "giddy", "harsh", "ingot", "joist",
    "knock", "leash", "mango", "noble", "oxide", "prism", "quirk", "relay", "swoop", "tweak",
    "untie", "vapor", "whirl", "xeric", "yogic", "zonal", "adept", "brisk", "chore", "douse",
    "ember", "flair", "gloss", "hinge", "ivory", "junta", "kiosk", "latch", "moron", "nylon",
    "opera", "prawn", "quail", "resin", "sloop", "tulip", "udder", "vixen", "wheat", "xenon",
    "yacht", "zephyr", "amuse", "brave", "coral", "dodge", "ethos", "flame", "grape", "hover",
    "irate", "joust", "karma", "lodge", "mirth", "nerve", "onion", "pique", "quota", "racer",
    "serum", "throb", "usher", "vista", "whale", "xerox", "yield", "zebra", "adept", "broom",
    "chill", "dolly", "elude", "frown", "glade", "honor", "image", "jumbo", "kudos", "lumen",
    "maple", "needy", "orbit", "poise", "quirk", "revel", "spine", "tweak", "unify", "verve",
    "waltz", "xeric", "youth", "zonal", "apple", "basil", "chime", "dwell", "epoch", "flint",
    "glory", "hazel", "ivory", "jumbo", "knoll", "latch", "mirth", "noble", "oasis", "pesto",
    "quirk", "rider", "swoop", "tempo", "urban", "vivid", "whisk", "xenon", "yodel", "zesty"
]


# the secret is picked randomly from the word list
secret = word_list[random.randint(0,len(word_list)-1)]

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
        print("Well done, you guessed the secret word!")
        print(f"Exiting in 5 seconds...")
        time.sleep(1)
        for second in range(5, 0, -1):
            print(f"{second}...")
            time.sleep(1)
        break
    
    # Prompt the user to enter another guess if needed
    guess = valid_guess()


            

