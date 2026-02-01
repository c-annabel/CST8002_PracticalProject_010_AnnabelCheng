"""
Docstring for main.py of Practical Project 1

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program applies fundamental concepts such as variables, methods, loops, file I/O, 
             exception handling, libraries, and array-like data structures.

Version: Python 3.14.2
Date: 2026.02.01

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject01

Reference: 
[1] 	W3Schools, "Python File Open," W3.CSS, [Online]. 
      Available: https://www.w3schools.com/python/python_file_handling.asp. [Accessed 24 1 2026].
[2] 	P. S. Foundation, "Input and Output," Python Software Foundation, [Online]. 
      Available: https://docs.python.org/3/tutorial/inputoutput.html. [Accessed 24 1 2026].
[3] 	J. Mertz, "Reading and Writing Files in Python (Guide)," DevCademy Media Inc. , [Online]. 
      Available: https://realpython.com/read-write-files-python/. [Accessed 24 1 2026].

"""
# Import the FileManager class from the file_manager package
from file_manager.FileManager import FileManager


def main():
   """Displays a looped main for file i/o operations."""

   # Store user name to display in the main
   user_name = "Annabel Cheng"
   filename = "pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"

   # Create an instance of FileManager to handle file reading and writing
   fm = FileManager()

   # Greet the user once at the start
   print(f"\nWelcome, {user_name}!")

   # Start the main loop
   while True: 
      # Display main options
      print("\n------ File I/O main ------")
      print("1. Read a file")
      print("2. Write a file")
      print("3. Exit")
      print("---------------------------\n")
      # Ask user for main choice
      choice = input("Enter your choice (1-3): ").strip()

      # Option 1: Read a file
      if choice == "1": 
         # Call FileManager to read file content
         content = fm.read_file(filename)
         # Display file content
         print("\n------ File Content ------")
         print(content)
      
      # Option 2: Write a file
      elif choice == "2": 
         text = input("\nEnter the info to write: ").strip()
         # Call FileManager to write the text to file
         fm.write_file(filename, text)

      # Option 3: Exit the program
      elif choice == "3":
         print(f"Goodbye, {user_name}!\n")
         break

      # Invalid input handling
      else: 
         print("Invalid choice. Please select 1, 2, or 3.")
    
# Run the main function only if this script is executed directly
if __name__ == "__main__":
   main()

# signoff info
print ("===========================================================") #Divider
print ("Message: Fundamental Python program for Practical Project 1") #Show main message.
print ("Version: Python 3.14.2")    #Show programming language used, and version.
print ("Author:  Annabel Cheng")    #show author's name as seen in ACSIS
print ("===========================================================\n") #Divider
