"""
Docstring for shorebird_monitoring_record.py of Practical Project 1

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program creates a class and uses the column names from the dataset
             as a reference for names of constants, variables, and accessors/mutators. 

Version: Python 3.14.2
Date: 2026.02.01

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject01

Reference: 
[1] 	W3Schools, "Python Classes and Objects," W3.CSS, [Online]. 
      Available: https://www.w3schools.com/python/python_classes.asp. [Accessed 30 1 2026].
[2] 	P. S. Foundation, "9. Classes" Python Software Foundation, [Online]. 
      Available: https://docs.python.org/3/tutorial/classes.html. [Accessed 31 1 2026].

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

   # A class method to display column headers of the dataset
   # Uses class-level data instead of object data, belongs to the class itself
   # Does not need an object to exist
   @classmethod
   def display_header(cls):
      return(
         f"{cls.COL_SITE_IDENTIFICATION} | " +
         f"{cls.COL_AREA} | " +
         f"{cls.COL_VISIT_DATE} | " +
         f"{cls.COL_START_TIME} | " +
         f"{cls.COL_SPECIES_CODE} | " +
         f"{cls.COL_COUNT} "
      )
   
   # A method to display record data from the dataset
   def display_record(self):
      return(
         f"{self.site_identification} | "
         f"{self.area} | "
         f"{self.visit_date} | "
         f"{self.start_time} | "
         f"{self.species_code} | "
         f"{self.count}."
      )