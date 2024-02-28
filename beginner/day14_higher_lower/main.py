import os
import random
from game_data import data
from art import logo, vs

## Create a function to select an item from the data list
def pick_one(data_list):
  return random.choice(data_list)
## Create a function to compare the follower_count field from the dictionaries
def compare_followers(item1, item2):
  """Compares the 'follower_count' field of 2 dictionaries and returns 1 if item 1 has more followers
  or 0 if item 2 has more followers."""

  if item1['follower_count'] > item2['follower_count']:
    return 1
  else:
    return 0

## Create a funtion for the game
def game():
  # Track game play
  keep_playing = True
  ## Store the score
  score = 0
  ## Pick two initial items from the data and save them as the things to compare
  A = pick_one(data)
  B = pick_one(data)
  while keep_playing:
    ## Make sure A and B aren't the same
    if A == B:
      # print("The options are the same...you should deal with that")
      B = pick_one(data)
    else:
      ## Print the two things to compare
      print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}.")
      print(vs)
      print(f"Compare B: {B['name']}, a {B['description']} from {B['country']}.\n")
      ## Compare the follower_count of the 2 dictionaries
      result = compare_followers(A, B)
      ## Ask for users choice
      user_choice = input("Who has more followers? Type 'A' or 'B': ")
      if (user_choice == 'A' and result == 1) or (user_choice == 'B' and result == 0):
        score += 1
        A = B
        B = pick_one(data)
        os.system('clear')
        # print(logo)
        print(logo)
        print(f"You're right! Current score: {score}.")
      else:
        os.system('clear')
        print(logo)
        print(f"You lost dummy! Your final score was {score}.")
        keep_playing = False

print(logo)
game()



## Use to clear the console
# os.system('clear')