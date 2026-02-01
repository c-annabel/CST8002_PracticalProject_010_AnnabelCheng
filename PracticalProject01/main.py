"""
Docstring for main.py of Practical Assessment 2

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: Provides a UI with a menu system for Practical Assessment 2 :
             displaying options to read/write files and calling file_manager.py
             to perform the actual file-io operations. 

Version: Python 3.14.2
Date: 2026.02.01

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalAssessment02

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


def menu():
   """Displays a looped menu for file i/o operations."""

   # Store user name to display in the menu
   user_name = "Annabel Cheng"

   # Create an instance of FileManager to handle file reading and writing
   fm = FileManager()

   # Greet the user once at the start
   print(f"\nWelcome, {user_name}!")

   # Start the main menu loop
   while True: 
      # Display menu options
      print("\n------ File I/O Menu ------")
      print("1. Read a file")
      print("2. Write a file")
      print("3. Exit")
      print("---------------------------\n")
      # Ask user for menu choice
      choice = input("Enter your choice (1-3): ").strip()

      # Option 1: Read a file
      if choice == "1": 
         filename = input("\nEnter the file name to read: ").strip()
         # Call FileManager to read file content
         content = fm.read_file(filename)
         # Display file content
         print("\n------ File Content ------")
         print(content)
      
      # Option 2: Write a file
      elif choice == "2": 
         text = input("\nEnter the info to write: ").strip()
         filename = input("\nEnter the file to write to: ").strip()
         # Call FileManager to write the text to file
         fm.write_file(filename, text)

      # Option 3: Exit the program
      elif choice == "3":
         print(f"Goodbye, {user_name}!\n")
         break

      # Invalid input handling
      else: 
         print("Invalid choice. Please select 1, 2, or 3.")
    
# Run the menu function only if this script is executed directly
if __name__ == "__main__":
   menu()

# signoff info
print ("-------------------------------------------------------") #Divider
print ("Message: File-IO program for Practical Assessment 2") #Show main message.
print ("Version: Python 3.14.2")    #Show programming language used, and version.
print ("Author:  Annabel Cheng")    #show author's name as seen in ACSIS
print ("-------------------------------------------------------\n") #Divider