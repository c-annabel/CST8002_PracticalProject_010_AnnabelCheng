"""
Module: record_memory_storage.py

Docstring for record_memory_storage.py of Practical Project 2
Modified for Practical Project 4

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description:
    This module defines the RecordStorage class, which represents
    the Business Layer of the application. It manages in-memory
    record objects and provides controlled access operations
    between the Presentation Layer and Persistence Layer.

    Project 4: 
    - Add get_unique_values() for returns a sorted list of unique valuesand 
    - Add get_unique_dates_sorted() returns visit dates sorted chronologically
    - Add filter_records() that filters in-memory records by species code text and 
    selected site, area, and visit date values.

Version: Python 3.14.3, pip 26.0.1, Flask 3.1.3
Due Date: 2026.04.12

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject04

Reference: 

[1] W3Schools. (n.d.). Python Modules. W3.CSS. [Online]. 
    Available at: https://www.w3schools.com/python/python_modules.asp
    [Accessed: Feb. 20, 2026]
[2] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. open.canada.ca. [Online]. 
    Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Feb. 18, 2026].
[3] Wong A. (Aug. 2, 2020). How to build a simple search engine using Flask. Medium. [Online]. 
    Available at: https://medium.com/analytics-vidhya/how-to-build-a-simple-search-engine-using-flask-4f3c01fe80fa 
    [Accessed: Apr. 1, 2026].
[4] Sofwan A. (Oct. 24, 2022). Creating Data Filter using Flask. Medium. [Online]. 
    Available at: https://medium.com/nerd-for-tech/creating-data-filter-using-flask-3f96c393b8df 
    [Accessed: Apr. 1, 2026].
[5] Pallets. (2010). Welcome to Flask — Flask documentation (3.1.x). Flask Official Documentation. Pallets. [Online]. 
    Available at: https://flask.palletsprojects.com/en/stable/ 
    [Accessed: Apr. 1, 2026].



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
    
    # Adding Search/Filter features for PP4 ----------------------------
    def get_unique_values(self, getter_name, records=None):
        """
        Returns a sorted list of unique values for a given field.
        If records is provided, unique values are derived from that
        list only — used to cascade dropdown options after filtering.

        Parameters:
            getter_name (str):       Name of the getter method to call.
            records     (list|None): Optional subset of records to scan.
                                     Defaults to all in-memory records.

        Returns:
            list[str]: Sorted list of unique non-empty values.
        """
        if records is None:
           records = self._records
        
        values = set()
        for record in records:
            val = getattr(record, getter_name)()
            if val:
                values.add(val.strip())
        return sorted(values)

    def get_unique_dates_sorted(self, records=None):
        """
        Returns visit dates sorted chronologically (earliest first).
        Tries multiple date formats before falling back to string sort.
        If records is provided, derives dates from that subset only.

        Parameters:
            records (list|None): Optional subset of records to scan.
                                 Defaults to all in-memory records.

        Returns:
            list[str]: Chronologically sorted list of unique date strings.
        """
        from datetime import datetime

        if records is None:
           records = self._records

        values = set()
        for record in records:
            val = record.get_visit_date()
            if val:
                values.add(val.strip())

        def parse_date(d):
            for fmt in ('%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y',
                        '%Y/%m/%d', '%d-%b-%Y', '%b-%d-%Y'):
                try:
                    return datetime.strptime(d, fmt)
                except ValueError:
                    continue
            return d  # fallback: string sort

        return sorted(values, key=parse_date)


    def filter_records(self, species_query, sites, areas, dates):
        """
        Filters in-memory records by species code text and selected
        site, area, and visit date values. All active filters are
        applied together (AND logic).

        Parameters:
            species_query (str):  Partial text to match against species code.
            sites         (list): Selected site identification values.
            areas         (list): Selected area values.
            dates         (list): Selected visit date values.

        Returns:
            list: Filtered list of ShorebirdMonitoringRecord objects.

        """
        results = self._records

        if species_query:
            q = species_query.lower()
            results = [
                r for r in results
                if q in r.get_species_code().lower()
            ]

        if sites:
            results = [
                r for r in results
                if r.get_site_identification() in sites
            ]

        if areas:
            results = [
                r for r in results
                if r.get_area() in areas
            ]

        if dates:
            results = [
                r for r in results
                if r.get_visit_date() in dates
            ]

        return results