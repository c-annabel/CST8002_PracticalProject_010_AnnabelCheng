"""
Module: record_memory_storage.py

Docstring for record_memory_storage.py of Practical Project 2

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description:
    This module defines the RecordStorage class, which represents
    the Business Layer of the application. It manages in-memory
    record objects and provides controlled access operations
    between the Presentation Layer and Persistence Layer.

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Due Date: 2026.02.22

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject02

Reference: 

[1] W3Schools. (n.d.). Python Modules. W3.CSS. [Online]. 
    Available at: https://www.w3schools.com/python/python_modules.asp
    [Accessed: Feb. 20, 2026]
[2] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. open.canada.ca. [Online]. 
    Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Feb. 18, 2026].

"""
# Import the FileHandler class to perform file input/output operations
from myapp.persistence.file_handler import FileHandler


class RecordStorage:
    """
    Business layer class responsible for storing record objects in memory
    and providing domain-level operations.

    Responsibilities:
        - Load records from persistence layer
        - Maintain sequential data structure (Python list)
        - Provide controlled access to records
        - Support add, edit, delete operations
        - Coordinate saving data back to file

    Attributes:
        _records (list): Internal list storing record objects.
        _total_loaded (int): Total number of records loaded from file.
    """

    def __init__(self):
        """
        Constructor for RecordStorage.

        Initializes:
            _records as an empty list.
            _total_loaded as 0.

        This constructor prepares the business layer
        to store records in memory.
        """
        self._records = []
        self._total_loaded = 0

    def load_from_data(self, filename, limit):
        """
        Loads records from the persistence layer.

        Parameters:
            filename (str): Name of the file to load data from.
            limit (int): Maximum number of records to load.

        Returns:
            None

        Side Effects:
            Updates internal _records list.
            Updates _total_loaded count.
        """
        repo = FileHandler()
        self._records, self._total_loaded = repo.read_file(filename, limit)

    def get_records(self):
        """
        Returns all stored record objects.

        Returns:
            list: List of record objects currently stored in memory.
        """
        return self._records

    def get_total_loaded(self):
        """
        Returns total number of records loaded from file.

        Returns:
            int: Number of records originally loaded.
        """
        return self._total_loaded

    def save_to_new_file(self):
        """
        Saves current in-memory records to a new file.

        Returns:
            bool: True if file write is successful, otherwise False.
        """
        repo = FileHandler()
        return repo.write_file(self._records)

    def get_record_by_index(self, index):
        """
        Retrieves a single record by its index position.

        Parameters:
            index (int): Position of record in the list.

        Returns:
            object | None:
                Record object if index is valid.
                None if index is invalid.
        """
        if 0 <= index < len(self._records):
            return self._records[index]
        return None

    def get_records_range(self, start, end):
        """
        Retrieves multiple records using index range (inclusive).

        Parameters:
            start (int): Starting index.
            end (int): Ending index (inclusive).

        Returns:
            list: List of record objects within specified range.
                  Returns empty list if range invalid.

        Notes:
            Performs second-layer validation to ensure
            indexes stay within valid bounds.
        """
        if start < 0:
            start = 0
        if end >= len(self._records):
            end = len(self._records) - 1
        if start > end:
            return []

        return self._records[start:end + 1]

    def add_record(self, record):
        """
        Adds a new record to the in-memory list.

        Parameters:
            record (object): Record object to add.

        Returns:
            None
        """
        self._records.append(record)

    def edit_record_by_index(
        self,
        index,
        site_identification=None,
        area=None,
        visit_date=None,
        start_time=None,
        species_code=None,
        count=None,
    ):
        """
        Updates selected fields of an existing record by index.

        Parameters:
            index (int): Position of record in the list.
            site_identification (str, optional)
            area (str, optional)
            visit_date (str, optional)
            start_time (str, optional)
            species_code (str, optional)
            count (str, optional)

        Returns:
            bool:
                True if update successful.
                False if index is invalid.

        Notes:
            Only fields with non-None values will be updated.
        """
        if not (0 <= index < len(self._records)):
            return False

        record = self._records[index]

        if site_identification is not None:
            record.set_site_identification(site_identification)

        if area is not None:
            record.set_area(area)

        if visit_date is not None:
            record.set_visit_date(visit_date)

        if start_time is not None:
            record.set_start_time(start_time)

        if species_code is not None:
            record.set_species_code(species_code)

        if count is not None:
            record.set_count(count)

        return True

    def delete_record_by_index(self, index):
        """
        Deletes a record from memory using index.

        Parameters:
            index (int): Position of record to delete.

        Returns:
            bool:
                True if record deleted successfully.
                False if index invalid.
        """
        if 0 <= index < len(self._records):
            del self._records[index]
            return True
        return False