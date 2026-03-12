"""
Docstring for __main__.py of Practical Assessment 04

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: 
    This module represents the Presentation Layer of the application.

    It provides the interactive console menu, collects user input, and delegates all data operations to the Business Layer.

    This module demonstrates:
        - Inheritance:  all animal objects share the base Animal class
        - Polymorphism: speak() is called on each animal object in a
                        single loop, producing different output per type

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

from myapp.business.animal_storage import AnimalStorage

# Constant defining the width of separator lines used in output formatting
sep_line_width = 85
# Constant of Python version
p_version = "Python 3.14.2"
# Constant of User's full name displayed in program output
user_name = "Annabel Cheng"
# Main Message of the program signoff
main_msg = "1.1. Inheritance and Polymorphism demo program for Practical Assessment 4"



def main():
    """
    Main function of the myapp program.

    This function:
        - Displays a welcome message
        - Shows a menu for the user to select an animal
        - Prompts the user to give the animal a name
        - Displays the animal's sound using speak()
        - Allows the user to add multiple animals
        - Displays a final summary of all animals and their sounds
        - Exits cleanly on user request

    Returns:
        None
    """



    storage = AnimalStorage()

    # Initial Greeting
    print (f"\nHello, {user_name}!\n") 
    print("Let's find out what sound your animals make.\n")

    while True:

        # ==============================
        # Display animal selection menu
        # ==============================
        print("=" * sep_line_width)
        print("  What animal are you?")
        print("-" * sep_line_width)
        for key, label in AnimalStorage.MENU_OPTIONS.items():
            print(f"  {key}. {label}")
        print("  5. View all animals")
        print("  6. Exit")
        print("=" * sep_line_width)

        choice = input("Enter your choice (1-6): ").strip()
        print("-" * sep_line_width)

        # ==============================
        # Option 1-4: Add an animal
        # ==============================
        if choice in AnimalStorage.MENU_OPTIONS:
            animal_type = AnimalStorage.MENU_OPTIONS[choice]
            name = input(f"Enter a name for your {animal_type}: ").strip()

            if name == "":
                name = animal_type

            animal = storage.create_animal(choice, name)

            print("-" * sep_line_width)
            print(animal.speak())
            print(f"{user_name}, {name} has been added!\n")
            print("-" * sep_line_width)

        # ==============================
        # Option 5: View all animals
        # This is where POLYMORPHISM is visible:
        # speak() is called on each object in one loop,
        # producing a different sound per animal type.
        # ==============================
        elif choice == "5":
            if storage.get_total() == 0:
                print("No animals added yet.\n")
            else:
                print(f"\n  {'Animal':<10} | {'Name':<15} | Sound\n")
                print("-" * sep_line_width)
                for animal in storage.get_animals():
                    print(
                        f"  {animal.ANIMAL_TYPE:<10} | "
                        f"{animal.get_name():<15} | "
                        f"{animal.speak()}"       
                    )
                print("-" * sep_line_width)
                print(f"  Total animals: {storage.get_total()}")
                print(f"  {user_name}, display completed.")
            print("-" * sep_line_width)

        # ==============================
        # Option 6: Exit
        # ==============================
        elif choice == "6":
            print(f"\nGoodbye, {user_name}!\n")

            # signoff info (Display your full name on screen so it always remains visible.)
            print ("=" * sep_line_width) #Divider
            print (f"Message: {main_msg}") #Show main message.
            print (f"Version: {p_version}")    #Show programming language used, and version.
            print (f"Author:  {user_name}")    #show author's name as seen in ACSIS
            print ("=" * sep_line_width, end="\n") #Divider

            break

        else:
            print("Invalid option. Please enter a number between 1 and 6.")
            print("-" * sep_line_width)



if __name__ == "__main__":
    main()








