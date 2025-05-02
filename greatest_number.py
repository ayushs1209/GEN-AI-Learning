def find_greatest(num1, num2, num3):
  """Finds the greatest of three numbers."""
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3

# Get input from the user
try:
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  num3 = float(input("Enter the third number: "))

  # Find the greatest number
  greatest = find_greatest(num1, num2, num3)

  # Print the result
  print(f"The greatest number is: {greatest}")

except ValueError:
  print("Invalid input. Please enter valid numbers.")
