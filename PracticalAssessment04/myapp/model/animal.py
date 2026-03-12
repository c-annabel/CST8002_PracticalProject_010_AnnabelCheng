"""
Docstring for animal.py of Practical Assessment 04

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description:This module defines the base Animal class, which represents the Model layer of the Animal Tracker application.
            It encapsulates the common attributes and behaviours shared by all animal types: name and speak().


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

class Animal: 
    """
    Base class representing a general animal.

    This class defines the common attributes and interface
    shared by all animal types. It is intended to be
    subclassed, not instantiated directly.

    Attributes:
        name (str): The name of the animal type.

    Demonstrates Inheritance:
        Child classes (Lion, Crow, Pig, Wolf) inherit the
        name attribute and get_name() method from this class
        without rewriting them.

    Demonstrates Polymorphism:
        speak() is defined here as a default implementation
        and overridden in each child class to return a
        type-specific animal sound.
    """


    """
    Constant: ANIMAL_TYPE (str)
    Purpose:  Identifies the animal type in display output.
              Overridden by each child class.
    """
    ANIMAL_TYPE = "Animal"

    def __init__(self,name):
        """
        Constructor for Animal.

        Initializes a new animal object with a name.

        Parameters:
            name (str): The name of the animal.

        Returns:
            None
        """
        self.name = name
    
    # ==============================
    # Accessor (Getter) Method
    # ==============================
    def get_name(self): 
        """
        Returns the animal's name.

        Returns:
            str: The name of the animal.
        """
        return self.name
    
    # ==============================
    # Mutator (Setter) Method
    # ==============================
    
    def set_name(self,name):
        """
        Updates the animal's name.

        Parameters:
            name (str): The new name.

        Returns:
            None
        """
        self.name = name
    
    # ==============================
    # Display Method (Polymorphism)
    # ==============================

    def speak(self):
        """
        Returns the sound this animal makes.

        This method provides a default implementation and is
        intended to be overridden by each child class to return
        the sound specific to that animal type.

        This is the key method that demonstrates POLYMORPHISM:
        calling speak() on any Animal object produces output
        specific to its actual type at runtime.

        Returns:
            str: A string describing the animal's sound.
        """
        return f"{self.name} makes a sound."