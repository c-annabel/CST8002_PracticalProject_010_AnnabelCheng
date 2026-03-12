"""
Docstring for crow.py of Practical Assessment 04

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This module defines the Crow class, which extends the base Animal class. It overrides the speak() method to return
             the sound specific to a crow.

             Demonstrates:
            - Inheritance:  Crow inherits name and get_name() from Animal
            - Polymorphism: Crow overrides speak() with its own sound

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

class Crow(Animal):
    """
    Child class representing a Crow

    Inherits from Animal and overrides speak() to return
    the sound a crow makes.

    Demonstrates Inheritance:
        Crow receives name and get_name() from Animal
        without rewriting them.

    Demonstrates Polymorphism:
        speak() is overridden here to return "Roar!"
        instead of the default Animal sound.
    """

    """
    Constant: ANIMAL_TYPE (str)
    Purpose:  Overrides the parent constant to identify
              this animal as a Crow.
    """
    ANIMAL_TYPE = "Crow"

    def __init__(self, name):
        """
        Constructor for Crow.

        Calls the parent Animal constructor using super()
        to initialize the name attribute.

        Parameters:
            name (str): The name of the crow.

        Returns:
            None
        """
        super().__init__(name)

    def speak(self):
        """
        Returns the sound a crow makes.

        Overrides the base Animal speak() method.
        This override is what demonstrates POLYMORPHISM —
        the same method name produces a crow-specific result.

        Returns:
            str: A string with the crow's name and sound.
        """
        return f"{self.name} the Crow says: Ahh! Ahh!"