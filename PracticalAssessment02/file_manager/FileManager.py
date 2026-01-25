"""
Docstring for FileManager.py of Practical Assessment 2

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: The program handles reading / writing operations. 

Version: Python 3.14.2
Date: 2026.01.24

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

import os

class FileManager: 
    #Provides file input/output operations for text files.
    def read_file(self, filename: str) -> str:
      
      #Reads the contents of a text file and returns it as a string.
      #Adds '.txt' if missing and checks file existence.

        if not filename.endswith(".txt"):
            filename += ".txt"
        if not os.path.exists(filename):
            return f"File '{filename}' does not exist."
        with open(filename, "r") as f:
            return f.read()
