## Task 1: Read a File and Handle Errors

This program (`Task1.py`) reads the contents of a text file named `sample.txt` and prints each line to the console. If the file does not exist, it gracefully handles the error and displays an appropriate message to the user.


**Features:**
- Opens and reads `sample.txt` line by line.
- Handles `FileNotFoundError` if the file is missing.

**Code Explanation:**
- The program uses a `try-except` block to handle errors.
- It attempts to open `sample.txt` for reading. If successful, it prints each line after stripping whitespace.
- If the file is not found, it catches the `FileNotFoundError` and prints an error message.

---

## Task 2: Write and Append Data to a File

This program (`Task2.py`) allows the user to write and append data to a file named `output.txt`. It first takes user input and writes it to the file, then takes additional input to append to the same file, and finally displays the complete contents of the file.


**Features:**
- Takes user input and writes it to `output.txt`.
- Appends more user input to the same file.
- Reads and prints the final content of `output.txt`.
- Handles errors during file operations gracefully.

**Code Explanation:**
- The program uses a `try-except` block to handle any errors during file operations.
- It first asks the user for input and writes it to `output.txt` (overwriting any existing content).
- It then asks for more input and appends this to the same file.
- Finally, it reads and prints all lines from `output.txt` to show the final content.
- Any exceptions during these operations are caught and displayed as error messages.
