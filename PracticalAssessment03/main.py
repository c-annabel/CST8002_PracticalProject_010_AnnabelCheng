"""
Docstring for main.py of Practical Assessment 03

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program demonstrates two test-cases using an assert (or similar) as part of the unit testing library. 
             The first test case should always pass, while the second test case should be configured to fail.

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Date: 2026.02.09

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalAssessment03

Reference: 
[1] 	W3Schools, "Python File Open," W3.CSS, [Online]. 
      Available: https://www.w3schools.com/python/python_file_handling.asp. [Accessed 24 1 2026].
[2] 	P. S. Foundation, "Input and Output," Python Software Foundation, [Online]. 
      Available: https://docs.python.org/3/tutorial/inputoutput.html. [Accessed 24 1 2026].

"""
# Constant defining the width of separator lines used in output formatting
sep_line_width = 85
# Constant of Python version
p_version = "Python 3.14.2"
# Constant of User's full name displayed in program output
user_name = "Annabel Cheng"
# Main Message of the program sign-off
main_msg = "Pytest unit testing program for Practical Assessment 3."

def pinapple_shop(pinapples: int) -> int:
    return pinapples * 5

def main():

   """
   Main function of the program.

   This function:
   - Unit Testing function that generates two sets of testing results. 

   """


  # signoff info (Display your full name on screen so it always remains visible.)
print ("=" * sep_line_width) #Divider
print (f"Message: {main_msg}") #Show main message.
print (f"Version: {p_version}")    #Show programming language used, and version.
print (f"Author: {user_name}")    #show author's name as seen in ACSIS
print ("=" * sep_line_width, end="\n") #Divider


# Run the main function only if this script is executed directly
if __name__ == "__main__":
   main()


