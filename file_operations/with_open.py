# with_open.py
# Demonstrates the recommended with open() method for automatic file closing.

# Using 'with open()' ensures the file is automatically closed even if errors occur.
try:
    with open('file_operations/my_file.txt', 'r') as file:
        content = file.read()
        print('File content using with open():')
        print(content)
except FileNotFoundError:
    print('Error: file_operations/my_file.txt not found. Please run write.py first.')

# The file is automatically closed when the 'with' block is exited.
print('File automatically closed after with block.')

