height = input()
weight = input()

num_height = float(height)
num_weight = float(weight)

bmi = num_weight / num_height ** 2

rounded_bmi = round(bmi)

print(rounded_bmi)
