import random

print("Welcome to the number guessing game.\n")
print("I'm thinking of a number between 1 and 100.\n")
mode = input("Do you want to play in easy (e) mode or hard (h) mode? ")

num_to_guess = random.randint(1, 100)
print(f"CHEAT: The number is {num_to_guess}")

if mode == 'e':
  num_guesses_left = 10
else:
  num_guesses_left = 5

while num_guesses_left > 0:
  guess = int(input("Guess a number: "))
  if guess < num_to_guess:
    print("Too low.")
    num_guesses_left -= 1
    print(f"You have {num_guesses_left} guesses left.")
  elif guess > num_to_guess:
    print("Too high.")
    num_guesses_left -= 1
    print(f"You have {num_guesses_left} guesses left.")
  elif guess == num_to_guess:
    print("You guessed it correctly!!")
    break
  else:
    print("I wasn't able to process that input. Please try again - guess a number between 1 and 100.")

if num_guesses_left == 0:
  print(f"Sorry, you lost! The number to guess was {num_to_guess}")
else:
  print("You won - congrats!")