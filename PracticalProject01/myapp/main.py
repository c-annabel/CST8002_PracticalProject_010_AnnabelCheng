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

"""
# Import the FileHandler class  to perform file input operations
from myapp.file_io.file_handler import FileHandler
# Import the ShorebirdMonitoringRecord entity class from the package
from myapp.entity.shorebird_monitoring_record import ShorebirdMonitoringRecord

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
print ("Message: Fundamental Python program for Practical Project 1") #Show main message.
print ("Version: Python 3.14.2")    #Show programming language used, and version.
print ("Author:  Annabel Cheng")    #show author's name as seen in ACSIS
print ("=" * sep_line_width, end="\n") #Divider
