# read.py
# Demonstrates reading the entire content of a file.

# Open a file in read mode ('r'). The file must exist.
try:
    file = open('file_operations/my_file.txt', 'r')

    # Read the entire content of the file
    content = file.read()

    # Print the content
    print('File content:')
    print(content)

    # Close the file
    file.close()
except FileNotFoundError:
    print('Error: file_operations/my_file.txt not found. Please run write.py first.')

