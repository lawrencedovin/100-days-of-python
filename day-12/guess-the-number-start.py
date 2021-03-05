from art import logo
from random import randint
import os

def check_answer(guess, answer):
    if guess > answer:
        print(f"{guess} is too high.")
    elif guess < answer:
        print(f"{guess} is too low.")
    else:
        print(f"Great job! you guessed the correct answer which was {answer}")

def clear():
    os.system("clear") # Linux - OSX
    os.system("cls") # Windows

def guess_number():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    difficulty = ''
    guess = 101

    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower()

    attempts = 10 if difficulty == 'easy' else 5

    while guess != answer and attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Guess a number between 1 and 100: '))
        check_answer(guess, answer)
        attempts -= 1

    if attempts == 0: print('You lose.')
    play_again = input("Play again? 'y' or 'n': ").lower()
    clear()
    if play_again == 'y': guess_number()

guess_number()