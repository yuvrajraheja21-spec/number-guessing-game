#number guessing game 2
def guess_number_2():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
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

    if attempts == max_attempts and guess != number:
        print(f"Sorry, you've used all your attempts. The number was {number}.")
