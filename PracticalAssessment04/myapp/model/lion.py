"""
Docstring for lion.py of Practical Assessment 04

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This module defines the Lion class, which extends the base Animal class. It overrides the speak() method to return
             the sound specific to a lion.

             Demonstrates:
            - Inheritance:  Lion inherits name and get_name() from Animal
            - Polymorphism: Lion overrides speak() with its own sound

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Date: 2026.03.11

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalAssessment04

Reference: 
[1] A. Ameyanagi. (May 25, 2025). Inheritance and Polymorphism. Python Tutorial. [Online]. 
Available at: https://ameyanagi.github.io/python-tutorial/en/book/book/08-inheritance.html [Accessed: Mar. 11, 2026].

[2] GeeksforGeeks. (Oct 9, 2025). Inheritance in Python. GeeksforGeeks. [Online].
    Available at: https://www.geeksforgeeks.org/python/inheritance-in-python/
    [Accessed: Mar. 11, 2026].

"""

from myapp.model.animal import Animal

class Lion(Animal):
    """
    Child class representing a Lion.

    Inherits from Animal and overrides speak() to return
    the sound a lion makes.

    Demonstrates Inheritance:
        Lion receives name and get_name() from Animal
        without rewriting them.

    Demonstrates Polymorphism:
        speak() is overridden here to return "Roar!"
        instead of the default Animal sound.
    """

    """
    Constant: ANIMAL_TYPE (str)
    Purpose:  Overrides the parent constant to identify
              this animal as a Lion.
    """
    ANIMAL_TYPE = "Lion"

    def __init__(self, name):
        """
        Constructor for Lion.

        Calls the parent Animal constructor using super()
        to initialize the name attribute.

        Parameters:
            name (str): The name of the lion.

        Returns:
            None
        """
        super().__init__(name)

    def speak(self):
        """
        Returns the sound a lion makes.

        Overrides the base Animal speak() method.
        This override is what demonstrates POLYMORPHISM —
        the same method name produces a lion-specific result.

        Returns:
            str: A string with the lion's name and sound.
        """
        return f"{self.name} the Lion says: Roar! Roar!"