# ## Syntax
# programming_dictionary = {
#   "bug": "An error in a program that prevents the program from running as expected.",
#   "function": "A piece of code that you can easily call over and over again.",
# }

# # Retrieving items
# print(programming_dictionary["bug"])

# # Adding new items
# programming_dictionary["loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# # Create an empty dictionary
# empty_dict = {}

# # Edit an item in a dictionary
# programming_dictionary["bug"] = "A new value for bug!"
# print(programming_dictionary["bug"])

# # Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lyon", "Nice", "Lille"]},
    "Germany": ["Berlin", "Hamburg"]
}

people = [
    {
        "name": "Matt",
        "date_of_birth": "08-30-1990"
    },
    {
        "name": "Paul",
        "date_of_birth": "07-10-1973"
    }
]
