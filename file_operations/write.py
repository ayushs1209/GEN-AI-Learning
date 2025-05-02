# write.py
# Demonstrates writing content to a file.

# Open a file in write mode ('w'). If the file does not exist, it will be created.
# If the file exists, its contents will be erased.
file = open('file_operations/my_file.txt', 'w')

# Write lines to the file
file.write('Hello, this is the first line.
')
file.write('This is the second line.
')

# Close the file. It is important to close files after you are done with them.
file.close()

print('Content written to file_operations/my_file.txt')

