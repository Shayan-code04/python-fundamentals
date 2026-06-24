import random 
secret_number = random.randint(1, 50)
guess=int(input("Guess the number between 1 and 50: "))
while (guess != secret_number):
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    guess=int(input("Guess the number between 1 and 50: ")) 
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        



    