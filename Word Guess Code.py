# Word Game

# Importing random to select a random entry from the text file (choice())
import random

#Outer loop to repeat game, initialize variables
wants_to_play = True
win_count = 0
loss_count = 0
featured_words = []

# Loop to allow the option to play again.
while wants_to_play == True:

    # Dictionary for words; starting out with just one word:
    #target_word = 'verisimilitude'

    f = open('english-words-unabridged.txt')
    sample = f.readlines()
    f.close()

    target_word = random.choice(sample).lower()

    # Tuple of guess word, guess list (starting with underscores), initialize guess counter
    # the while loop checks if the word is in the previous words list (featured_words) before moving on in the program
    target_in_featured_words = False
    while target_in_featured_words == False:
        temp_list = list(target_word)
        temp_list.remove('\n')

        target_word_letters = tuple(temp_list)
        target_word = ''.join(temp_list)
        if target_word not in featured_words:
            featured_words.append(target_word)

            guess_list = []
            for i in target_word_letters:
                guess_list.append("_")
            target_in_featured_words = True

    # Set up loop, ask for guess, print what they have discovered
    victory_bool = False    # initializing for the loop
    guess_counter = 7
    while guess_counter > 0 and victory_bool == False:
        print(guess_list)
        print("You have " + str(guess_counter) + " guesses left")
        current_guess = str(input("Please enter your guess  ")).lower()

    # checking if the guess is the correct word or a letter in the target word.
        if len(current_guess) > 1 and current_guess != target_word:  #if they guess a word and it is incorrect
            guess_counter = guess_counter - 1
            print("That was incorrect!")
        elif len(current_guess) > 1 and current_guess == target_word:  #if they guess a word that is correct
            victory_bool = True
        elif len(current_guess) == 1 and current_guess in target_word_letters: #if they guess a letter that is in the target word
            k = 0
            for i in target_word_letters:
                if current_guess == i:
                    j = target_word_letters.index(i, k)
                    guess_list[j] = current_guess
                k += 1
        elif len(current_guess) == 1 and current_guess not in target_word_letters:  #if they guess a letter not in the target word.
            guess_counter = guess_counter - 1
            print(current_guess + " was not in the answer word.")
        else:
            print("this should not run- line 38")
        

    # Victory or Failure
    if victory_bool == True:
        print("Congratulations, you win!")
        win_count += 1
    elif victory_bool == False:
        print("FAIL! The correct answer was   " + target_word)
        loss_count += 1
    else:
        print("This should not run- line 49")
    
    # See if they want to play again
    x = 1
    while x == 1:
        user_input = input("Do you want to go again? [y/n]")
        if user_input == 'y':
            x = 2
        elif user_input == 'n':
            x = 3
            wants_to_play = False
        else:
            x = 1
    
# Final result
print("You won " + str(win_count) + " games and lost " + str(loss_count) + " games. The featured words were: ")
print(featured_words)

