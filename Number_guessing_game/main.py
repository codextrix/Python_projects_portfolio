import random

down = int(input("Please enter the lower bound:"))
up = int(input("Please enter the upper bound:"))
print(f"You have 7 guesses to guess the number between {down} and {up}")

ch = 7
gs = 0

random_num = random.randint(down, up)
print("Please enter your guesses:")

while True:
    guess = int(input())
    ch -= 1
    gs += 1

    if guess > random_num:
        print('Too high! Try a lower number.')
    elif guess < random_num:
        print('Too low! Try a higher number.')
    elif guess == random_num:
        print(f'Correct! The number is {guess}. You guessed it in {gs} attempts.')
        break

    if ch < 1:
        print(f'Sorry! The number was {random_num}. Better luck next time.')
        break
