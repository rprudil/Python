# Hangman

import time
import random
import numbers

Name = input("What is your name? ")

print("Hello " + Name + ", welcome to Hangman.")
# Pause - wait
time.sleep(2)
print("Before we begin, here are the rules.")
# Pause - Wait
time.sleep(3)
print("1. You will have ten turns to guess a letter to spell out a word.")
# Pause - Wait
time.sleep(3)
print("2. If you do not guess the word in ten guesses, the game will reset with a new word.")
# Pause - wait
time.sleep(3)
print("3. If you guess the word within ten guesses, you win.")
# Pause - wait
time.sleep(2)
print("Have fun!")

# Pause - wait
time.sleep(2)

Prompt = "Alright " + Name + ", guess a letter: "
print(Prompt)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Word = ["raspberry", "blueberry", "blackberry", "strawberry", "gojiberry"]
Word = random.choice(Word)

letters = input()

TotalTurns = 10
Turn = 1

# Guessing Conditions
turn = 1

while turn <= 10 and letters in Word or letters not in Word:
    letters = input("Guess again!")
