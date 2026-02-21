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


[1] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. 
    open.canada.ca. [Online]. Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Jan. 24, 2026].
[2] W3Schools. (n.d.). Python File Open. W3.CSS. [Online]. 
    Available at: https://www.w3schools.com/python/python_file_handling.asp.
    [Accessed: Jan. 24, 2026].
[4] Python Software Foundation. (n.d.). Built-in Functions. Python Software Foundation. [Online]. 
    Available at: https://docs.python.org/3/library/functions.html#enumerate.
    [Accessed: Jan. 31, 2026].
[5] Python Software Foundation. (n.d.). csv — CSV File Reading and Writing. Python Software Foundation. [Online]. 
    Available at: https://docs.python.org/3/library/csv.html.
    [Accessed: Jan. 31, 2026].
[3] W3Schools. (n.d.). Python uuid Module. W3.CSS. [Online]. 
    Available at: https://www.w3schools.com/python/ref_module_uuid.asp.
    [Accessed: Feb. 21, 2026].

"""

import csv #a built-in Python Library, designed to read CSV files row by row
           #it splits each row into columns

import uuid #

from myapp.model.shorebird_monitoring_record import ShorebirdMonitoringRecord

class FileHandler: 
    """
        Persistence layer responsible for CSV File-IO operations.
        Provides file input/output operations for the assigned file.
        Return a list of ShorebirdMonitoringRecord objects.

        Responsibilities:
        - Open and read the CSV file using File-IO
        - Parse each CSV row into individual data elements
        - Create ShorebirdMonitoringRecord objects
        - Store record objects in a list
        - Return the list of records and a total record count
    """

    def read_file(self, filename, limit):      
        
        """
        Reads the CSV dataset and returns record objects.

        Parameters:
            filename (str): Dataset file name.
            limit (int): Maximum number of records to read from the file.
                         Default value is 100.

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
            with open(filename, mode="r", newline="", encoding="latin-1") as f:  #for csv doc
                reader = csv.DictReader(f)
        
                #Skip the French header row
                next(reader, None)  #with None, if file is empty, prevents StopIteration crash. 

                # Loop through CSV rows
                for i, row in enumerate(reader):
                    #enumerate: read items and automatically track their position (index).
                    #row: a dictionary from the CSV, not an object.
                    #will stop naturally when file ends. (if less than 100 records)

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

        # Error message when other unexpected read errors take place
        except Exception as e:
            print("Reading file error:", e)

        # Return the list of records and the total display count
        return records, totaldisplay
    

    
    def write_file(self, records):
        """
        Writes records to a new CSV file using a UUID filename.
        Returns the created filename.
        """
        new_filename = f"shorebird_memory_{uuid.uuid4()}.csv"

        try:
            with open(new_filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)

                # Header row (English)
                writer.writerow([
                    ShorebirdMonitoringRecord.COL_SITE_IDENTIFICATION,
                    ShorebirdMonitoringRecord.COL_AREA,
                    ShorebirdMonitoringRecord.COL_VISIT_DATE,
                    ShorebirdMonitoringRecord.COL_START_TIME,
                    ShorebirdMonitoringRecord.COL_SPECIES_CODE,
                    ShorebirdMonitoringRecord.COL_COUNT
                ])

                # Data rows
                for r in records:
                    writer.writerow([
                        r.get_site_identification(),
                        r.get_area(),
                        r.get_visit_date(),
                        r.get_start_time(),
                        r.get_species_code(),
                        r.get_count()
                    ])

        except Exception as e:
            print("Writing file error:", e)
            return None

        return new_filename