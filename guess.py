
#building a number guessing game
import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
#setting up tries
    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
