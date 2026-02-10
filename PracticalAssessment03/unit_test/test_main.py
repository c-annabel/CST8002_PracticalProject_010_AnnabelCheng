"""
Docstring for test_main.py of Practical Assessment 03

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program contains unit tests that validates two scenarios of the main program's behavior: 
            one test case is designed to consistently pass, while the other is intentionally configured to fail
            in order to demonstrate pytest's failure reporting. 

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

#import the tested module/function
from myapp.main import pinapple_discount

def test_discount_pass():
    """
    Tests that the pineapple discount function returns the correct
    discount rate when more than 10 pineapples are purchased.

    This test is expected to PASS because purchasing 15 pineapples
    should apply a 25% discount.
    """
    assert pinapple_discount(15) == 0.25


def test_discount_fail():
    """
    Tests the pineapple discount function with a small purchase amount.

    This test is intentionally designed to FAIL. The expected value (0.10)
    does not match the actual discount returned by the function,
    demonstrating how pytest reports failed test cases.
    """
    assert pinapple_discount(3) == 0.05