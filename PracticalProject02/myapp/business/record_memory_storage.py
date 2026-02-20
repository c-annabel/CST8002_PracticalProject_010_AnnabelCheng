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
   def load_from_data(self, filename, limit=10):
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