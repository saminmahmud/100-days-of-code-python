import random
from Hangman_Art import stages, logo
from Hangman_Words import word_list

print(logo)
chosen_word = random.choice(word_list)

display = []

for _ in range(len(chosen_word)):
    display.append("_")

stages.reverse()

print(stages[0])
print(display)

stages_position = int(0)

while stages_position < len(stages)-1 and "_" in display:
    # print(f'You can take minimum {(len(stages))-1 - stages_position} moves')

    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        flag = True
        for index, char in enumerate(chosen_word):
            if char == guess and display[index] == "_":
                display[index] = chosen_word[index]
                print(stages[stages_position])
                print(display)
                flag = False
                break
        if flag:
            stages_position += 1
            print(stages[stages_position])
            print(display)
    else:
        stages_position += 1
        print(stages[stages_position])
        print(display)

if "_" not in display:
    print("\n\t**********\n\tYou Win. 🎉\n\t**********")
else:
    print("\n\t*************\n\tYou lose. 😥\n\t*************")