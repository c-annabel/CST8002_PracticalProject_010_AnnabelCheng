"""
Docstring for pytest_unit_testing.py of Practical Project 2

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program applies fundamental concepts such as variables, methods, loops, file I/O, 
             exception handling, libraries, and array-like data structures.

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Date: 2026.02.15

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject02

Reference: 
[1] 	W3Schools, "Python File Open," W3.CSS, [Online]. 
      Available: https://www.w3schools.com/python/python_file_handling.asp. [Accessed 24 1 2026].
[2] 	P. S. Foundation, "Input and Output," Python Software Foundation, [Online]. 
      Available: https://docs.python.org/3/tutorial/inputoutput.html. [Accessed 24 1 2026].

"""
from sample import func;


def test_answer():
    assert func(3) == 5

def test_answer2():
    assert func(3) == 4