"""
Module: shorebird_monitoring_record.py

Docstring for shorebird_monitoring_record.py of Practical Project 2

Course: CST8002 Section 010 Programming Language Research Project
Professor: Stanley Pieda

Author: Annabel Cheng
Student ID: 041146557

Description:
    Defines the ShorebirdMonitoringRecord entity class.
    This class represents one row from the Shorebird dataset
    and encapsulates record attributes with accessor and mutator methods.

Version: Python 3.14.2
Due Date: 2026.02.22

GitHub Repo: 
https://github.com/c-annabel/CST8002_PracticalProject_010_AnnabelCheng/tree/main/PracticalProject02

Reference: 

[1] Parks Canada. (Oct. 1, 2017). Migratory Shorebird Habitat Use - Pacific Rim. 
    open.canada.ca. [Online]. Available at: https://open.canada.ca/data/en/dataset/e0aa39b6-67c0-4863-bdad-d74e73870697 
    [Accessed: Feb. 18, 2026].
[2] W3Schools. (n.d.). Python Classes and Objects. W3.CSS. [Online]. 
    Available at: https://www.w3schools.com/python/python_classes.asp.
    [Accessed: Jan. 30, 2026]
[3] W3Schools. (n.d.). Python String format() Method. W3.CSS. [Online]. 
    Available at: https://www.w3schools.com/python/ref_string_format.asp.
    [Accessed: Feb. 01, 2026]
[4] Python Software Foundation. (n.d.). 9. Classes. Python Software Foundation. [Online]. 
    Available at: https://docs.python.org/3/tutorial/classes.html.
    [Accessed: Feb. 01, 2026]

"""

class ShorebirdMonitoringRecord:
    """
    Entity class representing a single row in the Shorebird dataset.

    This class models one monitoring record and encapsulates
    dataset attributes using private instance variables
    with corresponding accessor (getter) and mutator (setter) methods.

    Design Notes:
        - Follows Entity/Model pattern in N-Layer architecture
        - Contains only data and basic formatting logic
        - Does not perform file operations or business rules

    Attributes:
        site_identification (str)
        area (str)
        visit_date (str)
        start_time (str)
        species_code (str)
        count (str)
    """

    # ==========================
    # Dataset Column Constants
    # ==========================

    """
    Constant: Column header names exactly as shown in the dataset file.
    These constants are used for display consistency and maintainability.
    """

    COL_SITE_IDENTIFICATION = "Site identification"
    COL_AREA = "Area"
    COL_VISIT_DATE = "Visit date"
    COL_START_TIME = "Start time"
    COL_SPECIES_CODE = "Species code"
    COL_COUNT = "Count"

    def __init__(
        self,
        site_identification,
        area,
        visit_date,
        start_time,
        species_code,
        count,
    ):
        """
        Constructor for ShorebirdMonitoringRecord.

        Initializes a new record object using values
        parsed from a dataset row.

        Parameters:
            site_identification (str): Site identification value.
            area (str): Monitoring area value.
            visit_date (str): Date of site visit.
            start_time (str): Start time of monitoring.
            species_code (str): Code representing bird species.
            count (str): Number of birds counted.

        Returns:
            None

        Notes:
            Each object stores its own independent copy of record data.
        """

        self.site_identification = site_identification
        self.area = area
        self.visit_date = visit_date
        self.start_time = start_time
        self.species_code = species_code
        self.count = count

    # ==========================
    # Accessor (Getter) Methods
    # ==========================

    def get_site_identification(self):
        """
        Returns the site identification value.

        Returns:
            str: Site identification.
        """
        return self.site_identification

    def get_area(self):
        """
        Returns the area value.

        Returns:
            str: Monitoring area.
        """
        return self.area

    def get_visit_date(self):
        """
        Returns the visit date.

        Returns:
            str: Visit date.
        """
        return self.visit_date

    def get_start_time(self):
        """
        Returns the start time.

        Returns:
            str: Start time of monitoring.
        """
        return self.start_time

    def get_species_code(self):
        """
        Returns the species code.

        Returns:
            str: Species code.
        """
        return self.species_code

    def get_count(self):
        """
        Returns the count value.

        Returns:
            str: Number of birds counted.
        """
        return self.count

    # ==========================
    # Mutator (Setter) Methods
    # ==========================

    def set_site_identification(self, site_identification):
        """
        Updates the site identification.

        Parameters:
            site_identification (str): New site identification value.

        Returns:
            None
        """
        self.site_identification = site_identification

    def set_area(self, area):
        """
        Updates the area value.

        Parameters:
            area (str): New area value.

        Returns:
            None
        """
        self.area = area

    def set_visit_date(self, visit_date):
        """
        Updates the visit date.

        Parameters:
            visit_date (str): New visit date.

        Returns:
            None
        """
        self.visit_date = visit_date

    def set_start_time(self, start_time):
        """
        Updates the start time.

        Parameters:
            start_time (str): New start time.

        Returns:
            None
        """
        self.start_time = start_time

    def set_species_code(self, species_code):
        """
        Updates the species code.

        Parameters:
            species_code (str): New species code.

        Returns:
            None
        """
        self.species_code = species_code

    def set_count(self, count):
        """
        Updates the count value.

        Parameters:
            count (str): New count value.

        Returns:
            None
        """
        self.count = count

    # ==========================
    # Display Methods
    # ==========================

    @classmethod
    def display_header(cls):
        """
        Returns formatted dataset column headers.

        This method belongs to the class (not an instance)
        and uses class-level constants.

        Returns:
            str: Formatted column header string.
        """
        return (
            f"{'Index':<6} | "
            f"{cls.COL_SITE_IDENTIFICATION:<20} | "
            f"{cls.COL_AREA:<5} | "
            f"{cls.COL_VISIT_DATE:<12} | "
            f"{cls.COL_START_TIME:<12} | "
            f"{cls.COL_SPECIES_CODE:<13} | "
            f"{cls.COL_COUNT:<5}"
        )

    def display_record(self):
        """
        Returns formatted string of this record's data.

        Uses fixed-width left-aligned formatting
        to match display_header() column structure.

        Returns:
            str: Formatted record row string.
        """
        return (
            f"{self.site_identification:<20} | "
            f"{self.area:<5} | "
            f"{self.visit_date:<12} | "
            f"{self.start_time:<12} | "
            f"{self.species_code:<13} | "
            f"{self.count:<5}"
        )