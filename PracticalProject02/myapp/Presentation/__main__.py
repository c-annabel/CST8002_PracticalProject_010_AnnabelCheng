"""
Docstring for __main__.py of Practical Project 2

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program applies fundamental concepts such as variables, methods, loops, file I/O, 
             exception handling, libraries, and array-like data structures.

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Date: 2026.02.20

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject02

Reference: 
[1] Holger Krekel and Pytest-Dev Team. (n.d.). Pytest: Helps you write better programs. 
    Pytest Documentation. [Online]. Available at: https://docs.pytest.org/en/stable [Accessed: Feb. 9, 2026].
[2] Python Software Foundation. (n.d.). Unittest — Unit testing framework. 
    Python Documentation. [Online]. Available at: https://docs.python.org/3/library/unittest.html [Accessed: Feb. 9, 2026].
[3] Tech With Tim. (Feb. 25, 2025). Please learn how to write tests in Python: Pytest tutorial. 
    YouTube. [Online]. Available at: https://www.youtube.com/watch?v=EgpLj86ZHFQ [Accessed: Feb. 9, 2026].
[4] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. 
    open.canada.ca. [Online]. Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Feb. 18, 2026].

"""
# Import the FileHandler class  to perform file input operations
from myapp.file_io.file_handler import FileHandler
# Import the ShorebirdMonitoringRecord entity class from the package
from myapp.Model.shorebird_monitoring_record import ShorebirdMonitoringRecord

# Constant defining the width of separator lines used in output formatting
sep_line_width = 85

def main():

   """
   Main function of the program.

   This function:
   - Displays a welcome message
   - Uses FileHandler to read the dataset on startup
   - Stores record objects in a list
   - Displays dataset headers and records in a formatted table
   - Shows the total number of records displayed
   - Repeats output until the user chooses to exit
   - Displays goodbye and signoff messages
   """

   # User's full name displayed in program output
   user_name = "Annabel Cheng"

   # Dataset filename
   filename = "pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"


   # Greet the user at program startup
   print(f"\nWelcome, {user_name}!")
   print()


   # Create an instance of FileHandler to handle file reading 
   fh = FileHandler()
   # Read the file and retrieve record objects and display count
   records, totaldisplay = fh.read_file(filename)

   # Start the main program loop (allows repeated viewing until user exits)
   while True: 

      # Display Title and table header
      print("\n" +"=" * sep_line_width)
      print("Shorebird Monitoring Records")
      print("-" * sep_line_width)
      # Another way to have a separator line to match exactly the header:
      # print("-" * len(ShorebirdMonitoringRecord.display_header()))
      # Display dataset column headers
      print(ShorebirdMonitoringRecord.display_header())
      print("-" * sep_line_width, end="\n")

      # Loop through the list of records and print each one
      for r in records:
         # r is a new variable created by the loop, represents one object from 
         #      the 'records' list
         # Output the record data on screen.
         print(r.display_record())

      # Display summary information
      print("-" * sep_line_width, end="\n")
      print(f"Total records displayed: {totaldisplay}")
      print("=" * sep_line_width, end="\n")

      # Ask user if they want to exit the program
      exit = input("\nWould you like to exit the program? (y/n): ").strip()

      # Exit the program
      if exit == "y":
         print(f"\nGoodbye, {user_name}!\n")
         break


# Run the main function only if this script is executed directly
if __name__ == "__main__":
   main()

# signoff info (Display your full name on screen so it always remains visible.)
print ("=" * sep_line_width) #Divider
print ("Message: Fundamental Python program for Practical Project 2") #Show main message.
print ("Version: Python 3.14.2")    #Show programming language used, and version.
print ("Author:  Annabel Cheng")    #show author's name as seen in ACSIS
print ("=" * sep_line_width, end="\n") #Divider
