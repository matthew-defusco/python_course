## Data Types

# num_char = len(input("What is your name?"))

# below would cause an error because num_char is an int and you can't
# concatenate strings and integers
# print ("Your name has " + num_char + " characters.")

# you can check the type of date with the type() function
## Type conversion
# new_num_char = str(num_char)
# print ("Your name has " + new_num_char + " characters.")
# int()
# float()

# Using two division symbols will "floor" the calculation and turn it into
# integer (as opposed to a float which it normally does)
# print(8//3)

## f-Strings
# score = 0
# height = 1.8
# isWinning = True
# print(f"Your score is {score}, your heigh is {height}, and your winning status is {isWinning}.")

## Project
# Tip calculator
print("Welcome to the Tip Calculator app!\n")
bill_total = float(input("How much was the total?\n"))
tip_percentage = int(input("How much do you want to tip?\n"))
num_people = int(input("How many people should share the cost?\n"))
price_per_person = round((bill_total + (1 * tip_percentage)) / num_people, 3)
print(f"Each person should pay: ${price_per_person:.2f}")



