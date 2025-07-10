"""
Course: CST8002 Programming Language Research Project
Professor: Tyler DeLay
Due Date: 2025-07-13
Author: Haoran Zu
Description: Part of solution for Practical Project 3
"""

from PersistenceLayer.data_record import DataRecord


class DetailedRecord(DataRecord):
    """
    A more detailed representation of a facility's data record,
    demonstrating polymorphism by overriding display().
    """

    def display(self):
        """
        Displays the record in a more detailed, multi-line format.
        """
        print("=== Facility Emissions Report ===")
        print(f"Facility: {self.facility_name}")
        print(f"Company: {self.company}")
        print(f"Location: {self.address}, {self.city}, {self.province}, {self.postal_code}")
        print(f"Coordinates: {self.latitude}, {self.longitude}")
        print(f"Emissions: {self.emissions} {self.units}")
        print(f"Year: {self.report_year}")
        print(f"Details: {self.facility_details}")
        print(f"Info: {self.facility_info}")
        print("===============================\n")