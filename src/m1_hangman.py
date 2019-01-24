"""
Hangman.

Authors: Greg Wenning and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

import random


with open('words.txt') as f:
    f.readline()
    string = f.read()
    words = string.split()

r = random.randrange(0, len(words))
word = words[r]
print(word)
secret_word = []
for k in range(len(word)):
    secret_word = secret_word + ['-']
print(secret_word)


guesses = int(input('How many unsuccessful choices do you want to allow? '))

while True:
    answer = input('What letter do you want to try? ')

    for k in range(len(word)):
        if word[k] == answer:
            print('Correct! You still have', guesses, 'unsuccessful guesses left before you lose.')
            secret_word[k] = answer
        break


    new_list = 
    for k in range(len(secret_word)):
        new_list = new_list + str(secret_word[k])
    if guesses == 0:
        print('You lose! The secret word was: ', word)
        break
    if secret_word == word:
        print('Congratulations! You guessed the secret word: ', word)
        break
    print('Here is what you currently know about the secret word:', new_list)
