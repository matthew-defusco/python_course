# # File not found
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     # print(a_dictionary["asdfasdf"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print("That key doesn't exist", error_message)
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")
#     print("This will always run.")
#     file.close()

height = float(input("Height: "))
weight = int(input("Weight (lbs): "))

if height > 3:
    raise ValueError("Human height should not be higher than 3 meters.")

bmi = weight / height**2

print(bmi)
