name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
print("The Love Calculator is calculating your score...")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

names = (name1 + name2).upper()
count_true = names.count('T') +  names.count('R') +  names.count('U') +  names.count('E') 
count_love = names.count('L') +  names.count('O') +  names.count('V') +  names.count('E')
score = count_true * 10 + count_love

if score <= 10 or score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
