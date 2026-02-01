"""
Docstring for FileHandler.py of Practical Project 1

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: The program handles reading / writing operations. 

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

import os

class FileHandler: 
    """Provides file input/output operations for text files."""

    def read_file(self, filename: str) -> str:      
        #Reads the contents of a text file and returns it as a string.
        #checks file existence.


        # Check if the file exists; if not, return a message
        if not os.path.exists(filename):
            return f"File '{filename}' does not exist."
        
        # Open the file safely using 'with' to avoid resource leaks
        with open(filename, "r") as f:
            return f.read()
        
    def write_file(self, filename: str, text: str) -> None:      
        #Writes the given text to a file.
        #checks if the file exists, and asks for overwrite confirmation.
        #If the user chooses not to overwrite, appends the text on a new line.


        # Check if the file already exists
        if os.path.exists(filename):

            #if user chooses Not to overwrite, append text to the end
               with open(filename, "a") as f:
                  f.write("\n"+text) # Add newline before appending
                  print(f"\nText added to '{filename}' successfully.\n")
               return # Exit function after appending
      

      
