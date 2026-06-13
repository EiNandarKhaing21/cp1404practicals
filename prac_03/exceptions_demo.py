"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When numerator or denominator is not an integer, a ValueError will occur.
2. When will a ZeroDivisionError occur?
When denominator is equal to zero, a ZeroDivisionError will occur.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
YES!
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")