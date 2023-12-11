# phase3w1codechallenge

This repository contains Python functions for 3 code challenges. Each challenge has specific task, and the functions provided aim to solve these tasks.
Challenge 1: Time Conversion
Write a function that takes an hour (1 to 12), minute (0 to 59), and period ("am" or "pm") as input and returns a four-digit string encoding the time in 24-hour format.

HOW TO TEST
result = convert_12hrs_24hrs(2, 30, "pm")
print(result)

Challenge 2: Exactly Two Positive
Create a function that takes three integers (a, b, and c) as arguments and returns True if exactly two of the three integers are positive numbers, and False otherwise.

HOW TO TEST
result = exactly_two_positive(-4, 8, -2)
print(result)
Challenge 3: Consonant Value
Implement a function that takes a lowercase string containing only alphabetic characters and no spaces. The function should return the highest value of consonant substrings based on assigned values (a=1, b=2, ..., z=26).

HOW TO TEST
result = consonant_value("abcde")
print(result)
