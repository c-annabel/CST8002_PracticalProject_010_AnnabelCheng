"""
Docstring for record_memory_story.py of Practical Project 2

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program stores records in memory (list) and provide operations.

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Date: 2026.02.20

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
# Import the FileHandler class  to perform file input operations
from myapp.persistence.file_handler import FileHandler

class RecordStorage:

   """
    Business layer class that stores records in memory and provides access operations.

    Responsibilities:
    - Load records from persistence layer
    - Maintain sequential data structure (list)
    - Provide record access to presentation layer

   """
   # Constructor
   def __init__(self):
      self._records = []       #sequential list in memory
      self._total_loaded = 0   # number of records loaded

   # Loading method
   def load_from_data(self, filename, limit):
      """Loads records from the persistence layer."""
      repo = FileHandler()
      self._records, self._total_loaded = repo.read_file(filename, limit)

   # Getters
   def get_records(self):
      """Returns all stored record objects."""
      return self._records
   
   def get_total_loaded(self):
      """Returns number of loaded records."""
      return self._total_loaded
   
   # Save to the new file
   def save_to_new_file(self):
      repo = FileHandler()
      return repo.write_file(self._records)
   
   # Get one record by index
   def get_record_by_index(self, index):
      """Returns one record by list index or None if invalid."""
      if 0 <= index < len(self._records):
         return self._records[index]
      return None
   
   # Get multiple records by index range
   def get_records_range(self, start, end):
      """Returns a slice of records from start to end (inclusive end)."""
      # Second layer of verification
      if start < 0: start = 0
      if end >= len(self._records): end = len(self._records) - 1
      if start > end: return []
      
      return self._records[start:end+1]
   
   # Add new record
   def add_record(self, record):
      """Adds a new record to in-memory list."""
      self._records.append(record)


   # This method updates selected field of an existing record in memory 
   # using setter methods while validating the record index.
   def edit_record_by_index(self, index,
                         site_identification=None,
                         area=None,
                         visit_date=None,
                         start_time=None,
                         species_code=None,
                         count=None):
      """
      Updates a record in memory by its index.

      Parameters:
         index (int): Position of the record in the list.
         site_identification (str, optional)
         area (str, optional)
         visit_date (str, optional)
         start_time (str, optional)
         species_code (str, optional)
         count (str, optional)

      Returns:
         bool: True if updated successfully, False if index invalid.
    
      """
      # Validate index
      if not (0 <= index < len(self._records)):
         return False

      record = self._records[index]

      # Update only fields that are not None
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