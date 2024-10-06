def cube_number(num):
    return num ** 3

# Get user input
try:
    user_input = float(input("Enter a number to cube: "))
    result = cube_number(user_input)
    print(f"The cube of {user_input} is {result}.")
except ValueError:
    print("Please enter a valid number.")
