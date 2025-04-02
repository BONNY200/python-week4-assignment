  
def modify_file():
    # Asks the user for the input filename
    filename = input("Enter the filename to read: ")

    try:
        # Here is ti Open the file for reading
        with open(filename, "r") as file:
            content = file.read()  # Read file content
        
        # here is to modify content 
        modified_content = content.upper()

        # here is to create a new filename for the modified file
        new_filename = "modified_" + filename

        # here is to write the modified content to a new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read. Please check file permissions.")

# here is to run the function
modify_file()
