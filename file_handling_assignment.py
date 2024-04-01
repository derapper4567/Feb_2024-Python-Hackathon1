# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("First line: Hello, World!\n")
        file.write("Second line: 12345\n")
        file.write("Third line: Python is great!\n")
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")
finally:
    file.close()

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")
finally:
    file.close()

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Fourth line: Appending some text!\n")
        file.write("Fifth line: 67890\n")
        file.write("Sixth line: Python file handling\n")
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")
finally:
    file.close()