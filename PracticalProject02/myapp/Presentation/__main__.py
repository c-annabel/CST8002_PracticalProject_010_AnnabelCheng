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
[1] W3Schools. (n.d.). Python File Open. Refsnes Data. [Online]. 
    Available at: https://www.w3schools.com/python/python_file_handling.asp
    [Accessed: Jan. 24, 2026].
[2] Python Software Foundation. (n.d.). Input and Output. Python Software Foundation. [Online]. 
    Available at: https://docs.python.org/3/tutorial/inputoutput.html
    [Accessed: Jan. 24, 2026].
[3] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. open.canada.ca. [Online]. 
    Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Feb. 18, 2026].

"""

# Import the ShorebirdMonitoringRecord entity class from the package
from myapp.model.shorebird_monitoring_record import ShorebirdMonitoringRecord
# Import the RecordStorage entity class from the package
from myapp.business.record_memory_storage import RecordStorage

# Constant defining the width of separator lines used in output formatting
sep_line_width = 95

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

   #number of records displayed
   limit = 100

   # Greet the user at program startup
   print(f"\nWelcome, {user_name}!")
   print()

   # Create business layer storage
   storage = RecordStorage()
   # Load records through business layer (not persistence directly)
   storage.load_from_data(filename, limit)

   # Start the main program loop (allows repeated viewing until user exits)
   while True: 

      # Create business layer storage
      records = storage.get_records()
      #Last record's index number
      last_index = len(records) - 1

      # Display menu options
      print("\n************ Practical Project 2 Menu ************")
      print("1. Reload data")
      print("2. Save data to a new csv file (UUID filename)")
      print("3. Display records")
      print("4. Create new record")
      print("5. Edit record")
      print("6. Delete record")
      print("7. Exit")
      print("*" * 50, end="\n")
      # Ask user for menu choice
      choice = input("Enter your choice (1-7): ").strip()

      print("-" * sep_line_width, end="\n")

      # Option 1 : Reload data
      if choice == "1":
         storage.load_from_data(filename, limit)
         print(f"Reloaded {storage.get_total_loaded()} records.")
         print("-" * sep_line_width, end="\n")   

      # Option 2 : Save to a new file with UUID file name
      elif choice == "2":
            new_file = storage.save_to_new_file()
            print(f"Saved to {new_file}.")
            print("-" * sep_line_width, end="\n")   

      # Option 3 : Select record(s) to display
      elif choice == "3":
            
         # Ask user to selection one or multiple records
         while True:
            display_type = input("(1) Display one record (2) Display multiple records? ").strip()
            print("-" * sep_line_width, end="\n")   

            if display_type not in ("1", "2"):
               print("Invalid option. Please choose 1 or 2.")
               print("-" * sep_line_width, end="\n")  
               continue

            # Display Option 1: Display one record
            if display_type == "1":
               # inner loop for single index
               while True:
                  try: 
                     record_index = int(input(f"Choose a record index (0-{last_index}): ").strip())
                     print("-" * sep_line_width, end="\n")  

                     if 0 <= record_index <= last_index:
                        print(f"You selected record {record_index}.")
                        print("-" * sep_line_width, end="\n")   

                        table_header_display()
                        r = storage.get_record_by_index(record_index)
                        print(f"{record_index:<6} | {r.display_record()}")
                        table_footer_display(1)
                        break
                     else:
                        print(f"Index must be between 0 and {last_index}.")
                        print("-" * sep_line_width, end="\n")  

                  except ValueError:
                     print("Invalid input. Please enter a number.")

               break

            # Display Option 2: Display multiple records
            elif display_type == "2":
               # inner loop for a range
               while True:
                  try:
                     record_range_start = int(input(f"Record index start from (0-{last_index}): ").strip())
                     record_range_end = int(input(f"Record index end with (0-{last_index}): ").strip())

                     if not (0 <= record_range_start <= last_index and 0 <= record_range_end <= last_index):
                        print(f"Indexes must be between 0 and {last_index}.")
                        print("-" * sep_line_width, end="\n")  
                        continue

                     if record_range_end < record_range_start:
                        print("End index must be greater than or equal to start index.")
                        print("-" * sep_line_width, end="\n")  
                        continue

                     print("-" * sep_line_width, end="\n")  
                     print(f"You selected records from {record_range_start} to {record_range_end}.")
                     print("-" * sep_line_width, end="\n")   
                     
                     table_header_display()
                     record_range = storage.get_records_range(record_range_start, record_range_end)
                     record_shown = len(record_range)
                     for index, r in enumerate(record_range, start = record_range_start):
                        print(f"{index:<6} | {r.display_record()}")
                     table_footer_display(record_shown)
                     
                     break

                  except ValueError:
                     print("Invalid input. Please enter numbers only.") 

               break
      # Option 4 : Add a record
      elif choice == "4":
  
            # Display questions for the new record
            site = input("Enter Site Identification: ").strip()
            area = input("Enter Area: ").strip()
            date = input("Enter Visit Date (DD/MM/YYYY): ").strip()
            time = input("Enter Sart Time (HH:MM:SS AM/PM): ").strip()
            code = input("Enter Species Code: ").strip()
            count = input("Enter Count: ").strip()
            new_rec = ShorebirdMonitoringRecord(site, area, date, time, code, count)
            storage.add_record(new_rec)

            print("Added a new record.")
            print("-" * sep_line_width, end="\n")   

      # Option 5 : Edit a record
      elif choice == "5":
            
            while True:
               try: 
                  record_index = int(input(f"Choose a record index (0-{last_index}): ").strip())
                  print("-" * sep_line_width, end="\n")  

                  if 0 <= record_index <= last_index:
                     print(f"You selected record to edit {record_index}.")
                     print("-" * sep_line_width, end="\n")   

                     table_header_display()
                     r = storage.get_record_by_index(record_index)
                     print(f"{record_index:<6} | {r.display_record()}")
                     print("-" * sep_line_width, end="\n")  

                     # Display questions for editing the requested record
                     site = input(f"Enter Site Identification [{r.get_site_identification()}]: ").strip()
                     if site == "": site = r.get_site_identification()
                     area = input(f"Enter Area [{r.get_area()}]: ").strip()
                     if area == "": area = r.get_area()
                     date = input(f"Enter Visit Date (DD/MM/YYYY) [{r.get_visit_date()}]: ").strip()
                     if date == "": date = r.get_visit_date()
                     time = input(f"Enter Sart Time (HH:MM:SS AM/PM) [{r.get_start_time()}]: ").strip()
                     if time == "": time = r.get_start_time()
                     code = input(f"Enter Species Code [{r.get_species_code()}]: ").strip()
                     if code == "": code = r.get_species_code()
                     count = input(f"Enter Count [{r.get_count()}]: ").strip()
                     if count == "": count = r.get_count()

                     # Varifying the values
                     # print(f"{site} | {area}| {date}| {time}| {code}| {count}")

                     success = storage.edit_record_by_index(
                        record_index,
                        site_identification=site,
                        area=area,
                        visit_date=date,
                        start_time=time,
                        species_code=code,
                        count=count
                     )

                     if success:
                        print(f"Record with index {record_index} updated successfully.")
                     else:
                        print("Invalid index.")
                     
                     print("-" * sep_line_width, end="\n")  

                     break
                  else:
                     print(f"Index must be between 0 and {last_index}.")
                     print("-" * sep_line_width, end="\n")  

               except ValueError:
                  print("Invalid input. Please enter a number.")
  


      # Option 7: Exit the program
      elif choice == "7":
            # Exit the program
            print(f"\nGoodbye, {user_name}!\n")
            break

      else:
            print("Invalid option!! ")
            continue
      
def table_header_display():
      # Display Title and table header
      print("\n" +"=" * sep_line_width)
      print("Shorebird Monitoring Records")
      print("-" * sep_line_width)
      # Another way to have a separator line to match exactly the header:
      # print("-" * len(ShorebirdMonitoringRecord.display_header()))
      # Display dataset column headers
      print(ShorebirdMonitoringRecord.display_header())
      print("-" * sep_line_width, end="\n")


def table_footer_display(totaldisplay):
      # Display summary information
      print("-" * sep_line_width, end="\n")
      print(f"Total records displayed: {totaldisplay}")
      print("=" * sep_line_width, end="\n")

# Run the main function only if this script is executed directly
if __name__ == "__main__":
   main()

# signoff info (Display your full name on screen so it always remains visible.)
print ("=" * sep_line_width) #Divider
print ("Message: Fundamental Python program for Practical Project 2") #Show main message.
print ("Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2")    #Show programming language used, and version.
print ("Author:  Annabel Cheng")    #show author's name as seen in ACSIS
print ("=" * sep_line_width, end="\n") #Divider
