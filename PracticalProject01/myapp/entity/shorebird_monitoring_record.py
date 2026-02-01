"""
Docstring for shorebird_monitoring_record.py of Practical Project 1

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program uses the column names from the dataset as part of the source code

Version: Python 3.14.2
Date: 2026.02.01

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject01

Reference: 
[1] 	W3Schools, "Python File Open," W3.CSS, [Online]. 
      Available: https://www.w3schools.com/python/python_file_handling.asp. [Accessed 24 1 2026].
[2] 	P. S. Foundation, "Input and Output," Python Software Foundation, [Online]. 
      Available: https://docs.python.org/3/tutorial/inputoutput.html. [Accessed 24 1 2026].
[3] 	J. Mertz, "Reading and Writing Files in Python (Guide)," DevCademy Media Inc. , [Online]. 
      Available: https://realpython.com/read-write-files-python/. [Accessed 24 1 2026].

"""


class ShorebirdMonitoringRecord:

   """
   Entity for one row in the provided dataset
   Column names are used as part of the variable names, accessors/mutators names, or constants. 
   """
   # Constants of dataset column names as shown in the file header
   COL_SITE_IDENTIFICATION = "Site identification"
   COL_AREA = "Area"
   COL_VISIT_DATE = "Visit date"
   COL_START_TIME = "Start time"
   COL_SPECIES_CODE = "Species code"
   COL_COUNT = "Count"

   # constructor that runs automatically each time create a new object from the class
   def __init__(self, site_identification, area, visit_date, start_time, species_code, count):
      #Take the parameters passed into the constructor and store them inside this object
      #Variables named after column names
      #self refers to the current object being created, allows each object to store 
      #     its own copy of data, similar to "this specific record"

      self.site_identification = site_identification
      self.area = area
      self.visit_date = visit_date
      self.start_time = start_time
      self.species_code = species_code
      self.count = count

   # Accessors (getters) named after column names
   def get_site_identification(self):
      return self.site_identification

   def get_area(self):
      return self.area

   def get_visit_date(self):
      return self.visit_date

   def get_start_time(self):
      return self.start_time

   def get_species_code(self):
      return self.species_code

   def get_count(self):
      return self.count

   # Mutators (setters) named after column names
   # self indicates THIS object
   def set_site_identification(self, site_identification):
      self.site_identification = site_identification

   def set_area(self, area):
      self.area = area

   def set_visit_date(self, visit_date):
      self.visit_date = visit_date

   def set_start_time(self, start_time):
      self.start_time = start_time

   def set_species_code(self, species_code):
      self.species_code = species_code

   def set_count(self, count):
      self.count = count

   # A method to display record data from the dataset
   def display_record(self):
      return(
         f"{self.COL_SITE_IDENTIFICATION}: {self.site_identification} | "
         f"{self.COL_AREA}: {self.area} | "
         f"{self.COL_VISIT_DATE}: {self.visit_date} | "
         f"{self.COL_START_TIME}: {self.start_time} | "
         f"{self.COL_SPECIES_CODE}: {self.species_code} | "
         f"{self.COL_COUNT}: {self.count}."
      )