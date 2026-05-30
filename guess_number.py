import random

answer = random.randint(1, 100)

guess = 0
error = 0

while guess != answer:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < answer:
        print("Too low! Try again.")
        error += 1
    elif guess > answer:
        print("Too high! Try again.")
        error += 1
    else:
        print(f"Congratulations! You've guessed the number! You've guessed {error} times!")    


wrong_guesses = []

wrong_guesses.append(guess)

high_guesses = [g for g in wrong_guesses if g > answer]
low_guesses = [g for g in wrong_guesses if g < answer]