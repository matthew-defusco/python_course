import os
from art import logo

print(logo)
bids = {}


def ask_for_bid():
  name = input("What is your name?:")
  bid = int(input("How much do you want to bid?: $"))

  bids[name] = bid

  another_bid = input("Are there any other bidders (yes/no)?: ")
  if another_bid == "yes":
    os.system('clear')
    ask_for_bid()
  if another_bid == "no":
    highest_bid = 0
    highest_bidder = ""
    for person in bids:
      if bids[person] > highest_bid:
        highest_bid = bids[person]
        highest_bidder = person
    print(f"The highest bid is {
          highest_bid} and that was the bid for {highest_bidder}.")
    print(f"Here are all the bids: {bids}")


ask_for_bid()
