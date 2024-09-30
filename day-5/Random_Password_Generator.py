# Python Loops
import random

print("Welcome to PyPassword Generator")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','.','-','_','@','#','$','%','&','*']

n_letters = int(input("How many letters would you like to your password? "))
n_symbols = int(input("How many symbols would you like? "))
n_numbers = int(input("How many numbers would you like? "))

password_list = []

for char in range(1, n_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, n_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, n_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

print(f'Password is: {"".join(password_list)}')
