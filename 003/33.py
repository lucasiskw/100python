height = input()
weight = input()

num_height = float(height)
num_weight = float(weight)

bmi = num_weight / num_height ** 2

rounded_bmi = round(bmi, 1)

print(f"Your BMI is {rounded_bmi}.")
if rounded_bmi < 18.5:
  (print("You are underweight."))
elif rounded_bmi < 25:
  (print("You are at a normal weight."))
elif rounded_bmi < 30:
  (print("You are slightly overweight."))
elif rounded_bmi < 35:
  (print("You are obese."))
else:
  (print("You are clinically obese."))
