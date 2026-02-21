"""
Docstring for test_main.py of Practical Project 2

Course: CST8002 Section 010
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description: This program contains unit tests that validates one scenarios of the main program's behavior: 
            one test case is designed to ensure that the program adds a new record into the sequential data structure.

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Date: 2026.02.21

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject2

Reference: 
[1] Holger Krekel and Pytest-Dev Team. (n.d.). Pytest: Helps you write better programs. 
    Pytest Documentation. [Online]. Available at: https://docs.pytest.org/en/stable [Accessed: Feb. 9, 2026].
[2] Python Software Foundation. (n.d.). Unittest — Unit testing framework. 
    Python Documentation. [Online]. Available at: https://docs.python.org/3/library/unittest.html [Accessed: Feb. 9, 2026].
[3] Tech With Tim. (Feb. 25, 2025). Please learn how to write tests in Python: Pytest tutorial. 
    YouTube. [Online]. Available at: https://www.youtube.com/watch?v=EgpLj86ZHFQ [Accessed: Feb. 9, 2026].

"""

import sys
import os

# Allow test to access project modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Import the ShorebirdMonitoringRecord entity class from the package
from myapp.model.shorebird_monitoring_record import ShorebirdMonitoringRecord
# Import the RecordStorage entity class from the package
from myapp.business.record_memory_storage import RecordStorage

def test_add_record():
    """
    Unit test: Verify that adding a new record
    increases the size of the in-memory list.
    """
    storage = RecordStorage()

    # Initial count
    initial_count = len(storage.get_records())

    # Create new record
    new_rec = ShorebirdMonitoringRecord(
        "TestSite",
        "2",
        "20/02/2026",
        "09:30:00 PM",
        "WILD",
        "8"
    )

    storage.add_record(new_rec)

    # New count
    new_count = len(storage.get_records())

    # Assert list size increased by 1
    assert new_count == initial_count + 1