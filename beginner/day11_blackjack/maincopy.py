import random

card_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def calculate_score(cards):
  score = 0
  for card in cards:
    if card == 'A' and score <= 10:
      score += 11
    elif card == 'A' and score > 11:
      score += 1
    elif card == 'J' or card == 'Q' or card == 'K':
      score += 10
    else:
      score += card
  return score


def get_card():
  return random.choice(card_list)


def play_game():
  play = input("Do you want to play blackjack?")
  if play == 'n':
    return

  dealer_hand = random.sample(card_list, 2)
  player_hand = random.sample(card_list, 2)

  dealer_score = calculate_score(dealer_hand)
  player_score = calculate_score(player_hand)

  print(f"The dealers cards are {dealer_hand} and their score is {dealer_score}")
  print(f"The players cards are {player_hand} and your score is {player_score}")

  if dealer_score < 16:
    dealer_hand.append(get_card())
    dealer_score = calculate_score(dealer_hand)

  get_another_card = input(
      "Do you want another card? Type 'y' for yes and 'n' for no.")

  if get_another_card == 'y':
    player_hand.append(get_card())
    player_score = calculate_score(player_hand)
    print(f"Your hand is {player_hand} and you have a score of {player_score}.")
    if player_score > 21:
      print(f"You lost! You went over 21. Your final hand was {player_hand} with a total score of {player_score}")
      print(f"The dealer's final hand was {dealer_hand} with a score of {dealer_score}.")
      play_game()
  elif get_another_card == 'n':
    if dealer_score > 21:
      print(f"You win! The dealer went over 21. Their final hand was {dealer_hand} with a total score of {dealer_score}.")
      print(f"Your final hand was {player_hand} with a score of {player_score}.")
      play_game()
    elif player_score > 21:
      print(f"You lost! You went over 21. Your final hand was {player_hand} with a total score of {player_score}")
      print(f"The dealer's final hand was {dealer_hand} with a score of {dealer_score}.")
      play_game()
    elif player_score > dealer_score:
      print(f"You win! The dealer's hand was {dealer_hand} with a total score of {dealer_score}.")
      print(f"Your final hand was {player_hand} with a score of {player_score}.")
      play_game()

play_game()