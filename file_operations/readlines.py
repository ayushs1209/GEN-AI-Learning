# readlines.py
# Demonstrates reading all lines of a file into a list.

# Open a file in read mode ('r').
try:
    file = open('file_operations/my_file.txt', 'r')

    # Read all lines into a list
    lines = file.readlines()

    # Print the list of lines
    print('File content as a list of lines:')
    print(lines)

    # Close the file
    file.close()
except FileNotFoundError:
    print('Error: file_operations/my_file.txt not found. Please run write.py first.')

