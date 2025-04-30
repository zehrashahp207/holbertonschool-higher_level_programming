#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Get the last digit
last_digit = number % 10 if number >= 0 else -(-number % 10)
# Determine the message based on the last digit
if last_digit > 5:
    result = f"Last digit of {number} is {last_digit} " \
             "and is greater than 5"
elif last_digit == 0:
    result = f"Last digit of {number} is {last_digit} and is 0"
else:
    result = f"Last digit of {number} is {last_digit} " \
             "and is less than 6 and not 0"
# Print the result
print(result)
