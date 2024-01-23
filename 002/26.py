# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

bill = input("What wat the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

num_bill = float(bill)
num_percentage = float(percentage)
num_people = float(people)

bill_with_tip = num_bill * (1 + num_percentage / 100)
bill_splitted = bill_with_tip / num_people
bill_splitted_rounded = f"{bill_splitted:.2f}"

print(f"Each person should pay: ${bill_splitted_rounded}")
