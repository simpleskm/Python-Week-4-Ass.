# error_handling_lab.py

try:
    filename = input("Enter the filename to open: ")
    with open(filename, "r") as file:
        content = file.read()
        print("File contents:\n")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
