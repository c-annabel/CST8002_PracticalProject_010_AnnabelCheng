"""
Docstring for file_handler.py of Practical Project 2

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: 
This module provides file input operations for reading the dataset 
and converting each row into record objects.

Version: Python 3.14.2
Date: 2026.02.19

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

import csv #a built-in Python Library, designed to read CSV files row by row
           #it splits each row into columns
from myapp.model.shorebird_monitoring_record import ShorebirdMonitoringRecord

class FileHandler: 
    """
        Provides file input/output operations for the assigned file.
        Return a list of ShorebirdMonitoringRecord objects.

        Responsibilities:
        - Open and read the CSV file using File-IO
        - Parse each CSV row into individual data elements
        - Create ShorebirdMonitoringRecord objects
        - Store record objects in a list
        - Return the list of records and a total record count
    """

    def read_file(self, filename, limit=10):      
        
        """
        Reads the CSV dataset and returns record objects.

        Parameters:
            filename (str): Dataset file name.
            limit (int): Maximum number of records to read from the file.
                         Default value is 10.

        Returns:
            tuple:
                - list[ShorebirdMonitoringRecord]: A list of record objects
                - int: Total number of records displayed
        """
        
        records = [] # List container to store record objects
        totaldisplay = 0 # Counter for total number of displayed records
        
        try:

            # The file is opened using Python File-IO (open)
            # Open the file safely using 'with' to avoid resource leaks
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
        
                #Skip the French header row
                next(reader)

                # Loop through CSV rows
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

                    # Create an object and store each part of the data into
                    # an instance of a record object’s fields,
                    # then append to the list/data structure. Each row is parsed and initializes one record object
                    record_obj = ShorebirdMonitoringRecord(c1, c2, c3, c4, c5, c6)
                    records.append(record_obj)
                    totaldisplay += 1
        
        # Prevents program crash:
        # Error message when the file is not found
        except FileNotFoundError: 
            print(f"Error: File '{filename}' not found.")

        # Error message when other or unexpected problemsread errors take place
        except Exception as e:
            print("Reading file error:", e)

        # Return the list of records and the total display count
        return records, totaldisplay
