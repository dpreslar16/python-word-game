# Word Game

# Dictionary for words; starting out with just one word:
target_word = 'verisimilitude'

# Tuple of guess word, guess list (starting with underscores), initialize guess counter
target_word_letters = tuple(list(target_word))
#print(target_word_letters)
#print(type(target_word_letters))

guess_counter = 7       # could set up as an input by user

guess_list = []
for i in target_word_letters:
    guess_list.append("_")
#print(guess_list)

