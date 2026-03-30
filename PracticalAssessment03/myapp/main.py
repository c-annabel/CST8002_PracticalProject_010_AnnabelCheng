"""
Docstring for main.py of Practical Assessment 03

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program demonstrates two test-cases using an assert (or similar) as part of the unit testing library. 
             The first test case should always pass, while the second test case should be configured to fail.

             The name is printed when the program is executed directly via main(), while pytest only imports the 
             module and runs test functions, so the program’s runtime output is not displayed during testing.

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Date: 2026.02.09

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalAssessment03

Reference: 
[1] Holger Krekel and Pytest-Dev Team. (n.d.). Pytest: Helps you write better programs. 
    Pytest Documentation. [Online]. Available at: https://docs.pytest.org/en/stable [Accessed: Feb. 9, 2026].
[2] Python Software Foundation. (n.d.). Unittest — Unit testing framework. 
    Python Documentation. [Online]. Available at: https://docs.python.org/3/library/unittest.html [Accessed: Feb. 9, 2026].
[3] Tech With Tim. (Feb. 25, 2025). Please learn how to write tests in Python: Pytest tutorial. 
    YouTube. [Online]. Available at: https://www.youtube.com/watch?v=EgpLj86ZHFQ [Accessed: Feb. 9, 2026].

"""
# Constant defining the width of separator lines used in output formatting
sep_line_width = 85
# Constant of Python version
p_version = "Python 3.14.2"
# Constant of User's full name displayed in program output
user_name = "Annabel Cheng"
# Main Message of the program signoff
main_msg = "Pytest unit testing program for Practical Assessment 3."


def pinapple_discount(pinapples: int) -> float:
    """
    Calculates the discount rate based on the number of pineapples purchased.

    If the number of pineapples is 10 or fewer, a 10% discount is applied.
    If more than 10 pineapples are purchased, a higher 25% discount is applied.

    Args:
        pinapples (int): The number of pineapples being purchased.

    Returns:
        float: The discount rate to be applied (e.g., 0.10 or 0.25).
    """
    if pinapples <= 10:
        return 0.10
    else:
        return 0.25
    

def main():

   """
   Main function of the program.

   This function:
   - Output relevant program info & Arthor's name.

   """

# signoff info (Display your full name on screen so it always remains visible.)
print ("=" * sep_line_width) #Divider
print (f"Message: {main_msg}") #Show main message.
print (f"Version: {p_version}")    #Show programming language used, and version.
print (f"Author:  {user_name}")    #show author's name as seen in ACSIS
print ("=" * sep_line_width, end="\n") #Divider


# Run the main function only if this script is executed directly
if __name__ == "__main__":
   main()


