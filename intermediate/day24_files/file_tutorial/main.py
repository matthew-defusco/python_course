# Manually opening and closing a file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Closes a file automatically
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# You can create a new file if it doesn't already exist with any name
with open("new_file.txt", mode="a") as file:
    file.write("New text.")