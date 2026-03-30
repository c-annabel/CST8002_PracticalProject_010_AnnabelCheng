"""
Docstring for animal_storagy.py of Practical Assessment 04

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: 
    This module defines the AnimalStorage class, which represents the Business Layer of the application.

    It manages the in-memory list of Animal objects selected by the user during the session, and provides controlled
    access operations between the Presentation Layer and Model Layer.

Architecture:
    Follows N-Layered architecture: Presentation → Business → Model

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

from myapp.model.lion import Lion
from myapp.model.crow import Crow
from myapp.model.wolf import Wolf
from myapp.model.pig import Pig

class AnimalStorage:
    """
    Business layer class responsible for managing Animal objects in memory.

    Responsibilities:
        - Create Animal objects based on user menu selection
        - Store Animal objects in a list
        - Provide access to the stored list
        - Clear the list when needed

    Attributes:
        _animals (list): Internal list storing Animal objects.
    """

    """
    Constant: MENU_OPTIONS (dict)
    Purpose:  Maps menu number strings to their display labels.
              Used by both the business layer and presentation layer.
    """
    MENU_OPTIONS = {
        "1": "Lion",
        "2": "Crow",
        "3": "Wolf",
        "4": "Pig"
    }

    def __init__(self):
        """
        Constructor for AnimalStorage.

        Initializes an empty list to store Animal objects.

        Returns:
            None
        """
        self._animals = []

    def create_animal(self, choice, name):
        """
        Creates an Animal object based on the user's menu choice
        and adds it to the internal list.

        Parameters:
            choice (str): The menu number chosen by the user ("1" to "4").
            name   (str): The name to assign to the animal.

        Returns:
            Animal | None:
                The created Animal object if choice is valid.
                None if the choice is not recognised.
        """
        animal = None

        if choice == "1":
            animal = Lion(name)
        elif choice == "2":
            animal = Crow(name)
        elif choice == "3":
            animal = Pig(name)
        elif choice == "4":
            animal = Wolf(name)

        if animal:
            self._animals.append(animal)

        return animal

    def get_animals(self):
        """
        Returns all Animal objects currently stored in memory.

        Returns:
            list: List of Animal objects.
        """
        return self._animals

    def get_total(self):
        """
        Returns the total number of animals stored.

        Returns:
            int: Number of Animal objects in the list.
        """
        return len(self._animals)

    def clear(self):
        """
        Clears all Animal objects from memory.

        Returns:
            None
        """
        self._animals.clear()