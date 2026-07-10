# numbers = []
# counter = 0
# while counter < 5:
#     try:
#         number = int(input("Number: "))
#         numbers.append(number)
#         counter += 1
#     except ValueError:
#         print("Input must be a valid number!")
#
# print(f"The first number is {numbers[0]}.")
# print(f"The last number is {numbers[4]}.")
# print(f"The smallest number is {min(numbers)}.")
# print(f"The largest number is {max(numbers)}.")
# print(f"The average of the numbers is {sum(numbers)/len(numbers)}.")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username: ")
if username in usernames:
    print("Access granted!")
else:
    print("Access denied!")
