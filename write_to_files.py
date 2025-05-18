# Write to a File
# This program creates a text file and writes content to it.

with open("example.txt", "w") as file:
    file.write("Hello! This is a sample file.\n")
    file.write("Writing to a file using Python is simple.\n")

print("Content written to 'example.txt'.")
