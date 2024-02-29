word_list = ["ardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)
guess_letter = input("Enter your guess: ").lower()

for letter in chosen_word:
    if letter == guess_letter:
        print("Right")
    else:
        print("Wrong")



