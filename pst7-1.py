import os
from datetime import datetime

def create_text_file_with_timestamp():
    """
    Create a text file with the current timestamp.
    """
    # Generate timestamp
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define file name with timestamp
    file_name = f"file_{current_time}.txt"

    # Create and write to the file
    with open(file_name, "w") as file:
        file.write("This is a text file created at " + current_time)
    
    # Return the file name
    return file_name

def main():
    # Create a text file with timestamp
    file_name = create_text_file_with_timestamp()

    # Print the created file name
    print(f"Text file with the current timestamp has been created: {file_name}")

if __name__ == "__main__":
    main()
