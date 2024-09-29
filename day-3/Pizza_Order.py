# Control Flow and Logical Operators

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L\n")
add_pepperoni = input("DO you want to pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
total_price = 0

if size == 'S':
    total_price += 15
elif size == 'M':
    total_price += 20
else:
    total_price += 25

if add_pepperoni == 'Y':
    if size == 'S':
        total_price += 2
    else:
        total_price += 3

if extra_cheese == 'Y':
    total_price += 1

print(f"Your total bill is ${total_price}")
