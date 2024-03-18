with open("./Input/Names/invited_names.txt") as name_file:
    names = [name.strip() for name in name_file]

with open("./Input/Letters/starting_letter.txt") as template_letter:
    contents = template_letter.read()
    for name in names:
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as new_letter:
            new_letter.write(contents.replace("[name]", name))

