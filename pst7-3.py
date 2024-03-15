def read_text_file(file_name):
    """
    Read content from the specified text file and display it in the console.
    """
    try:
        # Open the file in read mode
        with open(file_name, "r") as file:
            # Read the content of the file
            content = file.read()
            # Display the content in the console
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Get the name of the text file from the user
    file_name = input("Enter the name of the text file to read: ")
    # Call the function to read and display the content of the file
    read_text_file(file_name)

if __name__ == "__main__":
    main()
