"""
Module: test_main.py

Docstring for test_main.py of Practical Project 2

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description:
    Unit tests for the Business Layer (RecordStorage).

    This test verifies that adding a new record correctly
    increases the number of records stored in memory.

Testing Framework:
    Designed to be executed using pytest.

Architecture Context:
    This test interacts only with:
        - Entity Layer (ShorebirdMonitoringRecord)
        - Business Layer (RecordStorage)

    The Persistence Layer is not involved in this unit test.

Version: Python 3.14.2, pip 26.0.1, pytest 9.0.2
Due Date: 2026.02.22

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject2

Reference: 
[1] Holger Krekel and Pytest-Dev Team. (n.d.). Pytest: Helps you write better programs. 
    Pytest Documentation. [Online]. Available at: https://docs.pytest.org/en/stable [Accessed: Feb. 9, 2026].
[2] Python Software Foundation. (n.d.). Unittest — Unit testing framework. 
    Python Documentation. [Online]. Available at: https://docs.python.org/3/library/unittest.html [Accessed: Feb. 9, 2026].
[3] Tech With Tim. (Feb. 25, 2025). Please learn how to write tests in Python: Pytest tutorial. 
    YouTube. [Online]. Available at: https://www.youtube.com/watch?v=EgpLj86ZHFQ [Accessed: Feb. 9, 2026].
[4] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. 
    open.canada.ca. [Online]. Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Jan. 24, 2026].

"""

import sys
import os

"""
Purpose:
    Modify the Python path so that test files can access
    project modules located in the parent directory.

Reason:
    When running pytest from the test folder, Python
    may not automatically detect project packages.
"""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Import the ShorebirdMonitoringRecord entity class from the package
from myapp.model.shorebird_monitoring_record import ShorebirdMonitoringRecord
# Import the RecordStorage entity class from the package
from myapp.business.record_memory_storage import RecordStorage

def test_add_record():
    """
    Test Case:
        Verify that adding a new record increases
        the size of the in-memory record list.

    Steps:
        1. Create a RecordStorage instance.
        2. Record the initial number of stored records.
        3. Create a new ShorebirdMonitoringRecord object.
        4. Add the record to storage.
        5. Verify that the list size increases by one.

    Expected Result:
        The number of records after addition equals
        initial_count + 1.
    """
    # Create storage instance (empty in-memory list)
    storage = RecordStorage()

    # Get initial record count
    initial_count = len(storage.get_records())

    # Create a new record object
    new_rec = ShorebirdMonitoringRecord(
        "TestSite",
        "2",
        "20/02/2026",
        "09:30:00 PM",
        "WILD",
        "8"
    )
    
    # Add record to storage
    storage.add_record(new_rec)

    # Get updated record count
    new_count = len(storage.get_records())

    print("Author: Annabel Cheng")
    # Assert list size increased by 1
    assert new_count == initial_count + 1