# Randomisation and Python Lists

import random

hand_gestures = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

print("Welcome to Rock, Paper, Scissors Games")
user = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
print(hand_gestures[user])

computer = random.randint(0,2)
print(f"Computer choose {computer}")
print(hand_gestures[computer])

if user == computer:
    print("Draw!")
elif user == 0 and computer == 2:
    print("User wins!")
elif computer == 0 and user == 2:
    print("Computer wins!")
elif computer > user:
    print("Computer wins!")
else:
    print("User wins!")