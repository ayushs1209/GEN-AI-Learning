# readline.py
# Demonstrates reading a file line by line.

# Open a file in read mode ('r').
try:
    file = open('file_operations/my_file.txt', 'r')

    print('Reading file line by line:')
    # Read lines one by one until the end of the file
    while True:
        line = file.readline()
        if not line:
            break # End of file
        print(line, end='') # print the line, end='' avoids adding extra newline

    # Close the file
    file.close()
except FileNotFoundError:
    print('Error: file_operations/my_file.txt not found. Please run write.py first.')

