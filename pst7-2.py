from datetime import datetime

def create_text_file_with_timestamp_content():
    """
    Create a text file with the content of the current timestamp.
    """
    # Generate timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Define file name
    file_name = "timestamp.txt"

    # Create and write to the file
    with open(file_name, "w") as file:
        file.write("Current timestamp: " + current_time)
    
    # Return the file name
    return file_name

def main():
    # Create a text file with content of current timestamp
    file_name = create_text_file_with_timestamp_content()

    # Print the created file name
    print(f"Text file with the content of the current timestamp has been created: {file_name}")

if __name__ == "__main__":
    main()
