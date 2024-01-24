print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is you age? "))
  if age < 12:
    bill = 5
    print("Your ticket price is $5.")
  elif age < 18:
    bill = 7
    print("Your ticket price is $7.")
  elif age >= 45 and age <= 55:
    print("Your ticket price is $0.")
  else:
    bill = 12
    print("Your ticket price is $12.")
  wants_photo = input("Do you want a photo taker? Y or N. ")
  if wants_photo == 'Y':
    bill += 3
  print(f"Your final bill is ${bill}.")
else:
  print("Sorry, you have to grow taller before you can ride.")	
