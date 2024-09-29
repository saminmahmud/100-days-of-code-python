# Understanding Data Types and How to Manipulate Strings

print("Welcome to the tip calculator!")

# If the bill was $150.00, split between 5 people, with 12% tip.

bill = float(input("What is the total bill amount?\n$:"))
tip = float(input("How much tip would you like to give?\nPercent:"))
people = int(input("How many people to split the bill?\nPeople:"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

print(f"Each person should pay: ${bill_per_person:.2f}")