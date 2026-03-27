"""
Module: __routes__.py

Docstring for __routes__.py of Practical Project 3

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: 
    This module represents Flask framework, loading data from appointed data file. 

Version: 
        Python 3.14.3
        pip 26.0.1
        Flask 3.1.3
        Werkzeug 3.1.7
Due Date: 2026.03.29

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject03

Reference: 
[1] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. open.canada.ca. [Online]. 
    Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Feb. 18, 2026].
[2] Pallets. (2010). Welcome to Flask — Flask documentation (3.1.x). Flask Official Documentation. Pallets. [Online].
    Available at: https://flask.palletsprojects.com/en/stable/ 
    [Accessed: Mar. 20, 2026].
[3] GeeksforGeeks. (Mar. 7, 2026). Flask tutorial. GeeksforGeeks. [Online]. 
    Available at: https://www.geeksforgeeks.org/python/flask-tutorial/ 
    [Accessed: Mar. 20, 2026].

"""

from myapp import app
from myapp.business.record_memory_storage import RecordStorage

storage = RecordStorage()
filename = "pacific_rim_npr_coastalmarine_migratory_shorebird_habitat_use_2011-2017_data.csv"
storage.load_from_data(filename, 100)