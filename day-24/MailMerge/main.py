PLACEHOLDER = "[name]"

with open("./input/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./input/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        striped_name = name.strip()
        print(striped_name)
        new_letter = letter_contents.replace(PLACEHOLDER, striped_name)

        with open(f"./output/letter_for_{striped_name}.txt", 'w') as completed_letter:
            completed_letter.write(new_letter)
