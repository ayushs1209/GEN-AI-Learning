# append.py
# Demonstrates adding content to the end of an existing file.

# Open a file in append mode ('a'). If the file does not exist, it will be created.
# If the file exists, new content will be added to the end.
file = open('file_operations/my_file.txt', 'a')

# Write new lines to the file
file.write('This line is appended.
')
file.write('Another line is appended.
')

# Close the file
file.close()

print('Content appended to file_operations/my_file.txt')

