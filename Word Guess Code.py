# Word Game

import random

# Dictionary for words; starting out with just one word:
#target_word = 'verisimilitude'

f = open('english-words-unabridged.txt')
sample = f.readlines()


f.close()
target_word = random.choice(sample).lower()

# Tuple of guess word, guess list (starting with underscores), initialize guess counter
temp_list = list(target_word)
temp_list.remove('\n')

target_word_letters = tuple(temp_list)
target_word = ''.join(temp_list)


guess_list = []
for i in target_word_letters:
    guess_list.append("_")


guess_counter = 7       # could set up as an input by user


# Set up loop, ask for guess, print what they have discovered
victory_bool = False    # initializing for the loop

while guess_counter > 0 and victory_bool == False:
    print(guess_list)
    print("You have " + str(guess_counter) + " guesses left")
    current_guess = str(input("Please enter your guess  ")).lower()

# checking if the guess is the correct word or a letter in the target word.
    if len(current_guess) > 1 and current_guess != target_word:
        guess_counter = guess_counter - 1
        print("That was incorrect!")
    elif len(current_guess) > 1 and current_guess == target_word:
        victory_bool = True
    elif len(current_guess) == 1 and current_guess in target_word_letters:
        k = 0
        for i in target_word_letters:
            if current_guess == i:
                j = target_word_letters.index(i, k)
                guess_list[j] = current_guess
            k += 1
    elif len(current_guess) == 1 and current_guess not in target_word_letters:
        guess_counter = guess_counter - 1
        print(current_guess + " was not in the answer word.")
    else:
        print("this should not run- line 38")
    

# Victory or Failure
if victory_bool == True:
    print("Congratulations, you win!")
elif victory_bool == False:
    print("FAIL! The correct answer was   " + target_word)
else:
    print("This should not run- line 49")

