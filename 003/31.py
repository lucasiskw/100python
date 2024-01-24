# Which number do you want to check
number = int(input())

# Get the remainder of a number
odd_or_even = number % 2

# Check the remainder
if odd_or_even == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
