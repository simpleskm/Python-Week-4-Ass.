# file_read_write.py

def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()

        # Example modification: convert to uppercase
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"File '{input_file}' has been modified and saved as '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
input_filename = input("Enter the filename to read: ")
output_filename = "modified_" + input_filename
modify_file(input_filename, output_filename)
