# Function to check if a number is an Armstrong number
def is_armstrong(num):
    # Convert number to string to count digits
    num_str = str(num)
    n = len(num_str)
    sum_of_powers = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n
        temp //= 10
    return num == sum_of_powers

# Function to check if a number is a Palindrome number
def is_palindrome(num):
    # Convert number to string and check if it reads the same forwards and backwards
    num_str = str(num)
    return num_str == num_str[::-1]

# Function to check if a number is a Harshad (Niven) number
def is_harshad(num):
    # Calculate sum of digits
    temp = num
    sum_of_digits = 0
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit
        temp //= 10
    # A number is Harshad if it is divisible by the sum of its digits
    # Avoid division by zero if the sum of digits is 0 (only for num = 0, which is generally considered Harshad)
    if sum_of_digits == 0:
        return num == 0
    return num % sum_of_digits == 0

# Get user input
try:
    number = int(input("Enter an integer number: "))

    # Check and print results
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")

    if is_palindrome(number):
        print(f"{number} is a Palindrome number.")
    else:
        print(f"{number} is not a Palindrome number.")

    if is_harshad(number):
        print(f"{number} is a Harshad (Niven) number.")
    else:
        print(f"{number} is not a Harshad (Niven) number.")

except ValueError:
    print("Invalid input. Please enter an integer.")
