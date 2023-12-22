# ## if/else conditional
# print("Welcome to the rollercoaster!")
# height = int(input("How tall are you in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!\n")
#   age = int(input("How old are you? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5!")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7")
#   elif age >= 45 and age <= 55: # For people having a midlife crisis
#     print("Everything's going to be ok, have a free ride on us!")
#   else:
#     bull = 12
#     print("Adult tickets are $12")

#   wants_photo = input("Do you want a photo taken? (Y/N)\n")
#   if wants_photo == "Y":
#     bill += 3

#   print(f"Your total is ${bill}")

# else:
#   print(f"Sorry you're not quite tall enough! You have to be 120cm and you are only {height}cm")

# # combine conditions
# if age >= 15 and bill > 5:
#   print("Do something")
# elif age >= 12 or age <=5:
#   print("Do something else!")

## Project
# Treasure Island - Choose your own adventure game
print(r'''
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|)
''')
print("Welcome to Treasure Island - your mission is to find the treasure.\n")
left_right = input("Would you like to left or right? (r/l)\n")
if left_right == "r":
  print("Game over")
else:
  swim_wait = input("You come to a river. Would you like to swim across or wait for a boat? (swim/wait)\n")
  if swim_wait == "swim":
    print("Game over")
  else:
    door_choice = input("You encounter three doors that look identical. Which one do you choose? (1/2/3)\n")
    if door_choice == "1" or door_choice == "2":
      print("Game over")
    else:
      print(r'''
      *******************************************************************************
                |                   |                  |                     |
      _________|________________.=""_;=.______________|_____________________|_______
      |                   |  ,-"_,=""     `"=.|                  |
      |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
      _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
      |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
      |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
      _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
      |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
      |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
      ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
      /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
      ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
      /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
      ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
      /______/______/______/______/______/______/______/______/______/______/[TomekK]
      *******************************************************************************
      ''')
      print("You found the treasure and you win!!")
