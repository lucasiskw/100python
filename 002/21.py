two_digit_number = input()

str_first_digit = two_digit_number[0]
str_second_digit = two_digit_number[-1]

num_first_digit = int(str_first_digit)
num_second_digit = int(str_second_digit)

num_sum = (num_first_digit + num_second_digit)

print(num_sum)
