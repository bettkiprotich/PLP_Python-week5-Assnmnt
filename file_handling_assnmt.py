# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("This is line 2 with a number: 42.\n")
            file.write("Line 3: Python file handling is interesting!\n")
        print("File created and content written successfully.")
    except (PermissionError, Exception) as e:
        print(f"Error creating file: {e}")
    finally:
        print("Finished file creation process.")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("File contents:\n", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("Finished file reading process.")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending line 1: Goodbye!\n")
            file.write("Appending line 2: Numbers can also be fun: 100.\n")
            file.write("Appending line 3: Let's learn more about file handling.\n")
        print("Content appended successfully.")
    except (PermissionError, Exception) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("Finished file appending process.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to display the updated contents
