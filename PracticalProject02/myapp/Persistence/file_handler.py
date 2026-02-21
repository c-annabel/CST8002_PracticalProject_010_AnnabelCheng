"""
Module: file_handler.py

Docstring for file_handler.py of Practical Project 2

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description:
    This module defines the FileHandler class, which represents
    the Persistence Layer of the application.

    It is responsible for handling CSV file input and output operations.
    The class reads dataset rows, converts them into
    ShorebirdMonitoringRecord objects, and writes in-memory
    records back to a new CSV file.

Architecture:
    This module belongs to the Persistence Layer in an N-Layered design.
    It does not contain business logic or presentation logic.

Version: Python 3.14.2
Due Date: 2026.02.22

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

# Built-in Python library for CSV file processing
import csv

# Built-in Python library for generating unique identifiers
import uuid

from myapp.model.shorebird_monitoring_record import ShorebirdMonitoringRecord


class FileHandler:
    """
    Persistence layer class responsible for CSV file I/O operations.

    Responsibilities:
        - Open and read CSV files
        - Parse rows into structured data
        - Instantiate ShorebirdMonitoringRecord objects
        - Return list of entity objects
        - Write in-memory records back to CSV format

    This class does NOT:
        - Apply business rules
        - Format display output
        - Handle user interaction
    """

    def read_file(self, filename, limit):
        """
        Reads a CSV dataset file and converts rows into record objects.

        Parameters:
            filename (str): Name or path of the CSV file to read.
            limit (int): Maximum number of records to load into memory.

        Returns:
            tuple:
                - list[ShorebirdMonitoringRecord]:
                  List of created record objects.
                - int:
                  Total number of records successfully loaded.

        Behavior:
            - Uses csv.DictReader to map column names to values.
            - Skips the French header row.
            - Stops reading once limit is reached.
            - Handles file-not-found and unexpected read errors.

        Exceptions Handled:
            FileNotFoundError
            Generic Exception
        """

        records = []
        totaldisplay = 0

        try:
            with open(filename, mode="r", newline="", encoding="latin-1") as f:
                reader = csv.DictReader(f)

                # Skip optional French header row if present
                next(reader, None)

                for i, row in enumerate(reader):

                    if i >= limit:
                        break

                    c1 = row.get(
                        ShorebirdMonitoringRecord.COL_SITE_IDENTIFICATION, ""
                    ).strip()
                    c2 = row.get(
                        ShorebirdMonitoringRecord.COL_AREA, ""
                    ).strip()
                    c3 = row.get(
                        ShorebirdMonitoringRecord.COL_VISIT_DATE, ""
                    ).strip()
                    c4 = row.get(
                        ShorebirdMonitoringRecord.COL_START_TIME, ""
                    ).strip()
                    c5 = row.get(
                        ShorebirdMonitoringRecord.COL_SPECIES_CODE, ""
                    ).strip()
                    c6 = row.get(
                        ShorebirdMonitoringRecord.COL_COUNT, ""
                    ).strip()

                    record_obj = ShorebirdMonitoringRecord(
                        c1, c2, c3, c4, c5, c6
                    )

                    records.append(record_obj)
                    totaldisplay += 1

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

        except Exception as e:
            print("Reading file error:", e)

        return records, totaldisplay

    def write_file(self, records):
        """
        Writes in-memory records to a new CSV file.

        A unique filename is generated using UUID to prevent overwriting
        existing files.

        Parameters:
            records (list[ShorebirdMonitoringRecord]):
                List of record objects to be written.

        Returns:
            str:
                Name of the newly created file if successful.
            None:
                If writing fails.

        Behavior:
            - Writes English column headers.
            - Extracts values using getter methods.
            - Saves file in UTF-8 encoding.
        """

        new_filename = f"shorebird_memory_{uuid.uuid4()}.csv"

        try:
            with open(new_filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)

                writer.writerow([
                    ShorebirdMonitoringRecord.COL_SITE_IDENTIFICATION,
                    ShorebirdMonitoringRecord.COL_AREA,
                    ShorebirdMonitoringRecord.COL_VISIT_DATE,
                    ShorebirdMonitoringRecord.COL_START_TIME,
                    ShorebirdMonitoringRecord.COL_SPECIES_CODE,
                    ShorebirdMonitoringRecord.COL_COUNT
                ])

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