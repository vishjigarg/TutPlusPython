"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""
import os
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'output.txt')
    user_input = input("Enter data to write to the file: ")
    
    with open(file_path, 'w') as file:
        file.write(user_input + '\n')
    
    additional_data = input("Enter additional data to append to the file: ")
    
    with open(file_path, 'a') as file:
        file.write(additional_data + '\n')
    
    with open(file_path, 'r') as file:
        print("Final content of the file:")
        for line in file:
            print(line.strip())
        
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")