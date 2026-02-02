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
# Import the FileHandler class from the package
from myapp.file_io.file_handler import FileHandler
# Import the ShorebirdMonitoringRecord class from the package
from myapp.entity.shorebird_monitoring_record import ShorebirdMonitoringRecord


def main():
   """Displays a looped main for file i/o operations."""

   # Store user name to display in the main
   user_name = "Annabel Cheng"
   filename = "pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"

   # Greet the user once at the start
   print(f"\nWelcome, {user_name}!")
   print("=" * 60, end="\n")


   # Create an instance of FileHandler to handle file reading and writing
   fh = FileHandler()
   # Call FileHandler to read file content
   records = fh.read_file(filename)

   # Start the main loop
   while True: 

      # Display Title
      print("Shorebird Monitoring Records")
      print(ShorebirdMonitoringRecord.display_header())
      print("=" * 60)

      # for r in records:
      #    #r is a new variable created by the loop, represents one object from 
      #    #  the 'records' list
      #    print(r.display_record())

      print("=" * 60, end="\n")

      # Ask user if they want to exit the program
      exit = input("Would you like to exit the program? (y/n)").strip()

      # Exit the program
      if exit == "y":
         print(f"\nGoodbye, {user_name}!\n")
         break


# Run the main function only if this script is executed directly
if __name__ == "__main__":
   main()

# signoff info
print ("=============================================================") #Divider
print ("Message: Fundamental Python program for Practical Project 1") #Show main message.
print ("Version: Python 3.14.2")    #Show programming language used, and version.
print ("Author:  Annabel Cheng")    #show author's name as seen in ACSIS
print ("=============================================================\n") #Divider
