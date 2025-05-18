# Read from a File
# This program reads content from a file and prints it.

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print("File not found. Please run 'write_to_file.py' first.")
