"""
Docstring for FileHandler.py of Practical Project 1

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: The program handles file reading operations. 

Version: Python 3.14.2
Date: 2026.02.01

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject01

Reference: 
[1] 	W3Schools, "Python File Open," W3.CSS, [Online]. 
      Available: https://www.w3schools.com/python/python_file_handling.asp. [Accessed 24 1 2026].
[2] 	P. S. Foundation, "Built-in Functions" Python Software Foundation, [Online]. 
      Available: https://docs.python.org/3/library/functions.html#enumerate. [Accessed 31 1 2026].
[3] 	P. S. Foundation, "csv — CSV File Reading and Writing" Python Software Foundation, [Online]. 
      Available: https://docs.python.org/3/library/csv.html. [Accessed 31 1 2026].

"""

import csv #a built-in Python Library, designed to read CSV files row by row
           #it splits each row into columns
from myapp.entity.shorebird_monitoring_record import ShorebirdMonitoringRecord

class FileHandler: 
    """
        Provides file input/output operations for the assigned file.
        Return a list of ShorebirdMonitoringRecord objects.
    """

    def read_file(self, filename, limit=10):      
        
        #Reads the contents of a file and returns it as a list
        
        records = [] # create a list container
        totaldisplay = 0 # count total displayed records
        
        try:

            # Open the file safely using 'with' to avoid resource leaks
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
        
                #Skip French header row
                next(reader)

                for i, row in enumerate(reader):
                    #enumerate: read items and automatically track their position (index).
                    #row: a dictionary from the CSV, not an object.

                    #Skip French header row
                    # if i == 0:
                    #     continue

                    #Limit the number of records to show for easy presentation
                    if i >= limit:
                        break

                    # Separate record into separate data items using column names
                    c1 = row.get(ShorebirdMonitoringRecord.COL_SITE_IDENTIFICATION, "").strip()
                    c2 = row.get(ShorebirdMonitoringRecord.COL_AREA, "").strip()
                    c3 = row.get(ShorebirdMonitoringRecord.COL_VISIT_DATE, "").strip()
                    c4 = row.get(ShorebirdMonitoringRecord.COL_START_TIME, "").strip()
                    c5 = row.get(ShorebirdMonitoringRecord.COL_SPECIES_CODE, "").strip()
                    c6 = row.get(ShorebirdMonitoringRecord.COL_COUNT, "").strip()

                    # Create an object and store/append the data in the list
                    record_obj = ShorebirdMonitoringRecord(c1, c2, c3, c4, c5, c6)
                    records.append(record_obj)
                    totaldisplay += 1


        # Error message when the file is not found
        except FileNotFoundError: 
            print(f"Error: File '{filename}' not found.")

        # Error message when other problems take place
        except Exception as e:
            print("Reading file error:", e)


        return records, totaldisplay
