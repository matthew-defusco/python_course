## Random module
# import random
# import day4_module
# print(day4_module.pi)

# random_integer = random.randint(1, 10)
# print("Random int: ", random_integer)

# random_float = random.random() # generates a random number between 0 and 1 (not inclusive)
# print("Random float:", random_float * 5) # prints a random float between 0 and 5 (not inclusive)

# love_score = random.randint(1, 100)
# print("Your love score is", love_score)

## Lists
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
# print(states_of_america[0])

# states_of_america[1] = "Pencilvania"
# states_of_america.append("Mattville")
# states_of_america.extend(["Another One", "And The Second One", "Pepsitown"])
# print(states_of_america)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

## Project
# Rock, Paper, Scissors!
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
print("Welcome to RPS!\n")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
game_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number. You lose!")
else:
  print("You chose:\n", game_images[user_choice])
  print("Computer chose:\n", game_images[game_choice])

  if (user_choice == 0 and game_choice == 1) or (user_choice == 1 and game_choice == 2) or (user_choice == 2 and game_choice == 0):
    print("You lose!")
  elif user_choice == game_choice:
    print("It's a tie!")
  else:
    print("You win!")




