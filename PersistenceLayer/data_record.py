"""
Course: CST8002 Programming Language Research Project
Professor: Tyler DeLay
Due Date: 2025-07-13
Author: Haoran Zu
Description: Part of solution for Practical Project 3
"""

from PersistenceLayer.base_record import BaseRecord


class DataRecord(BaseRecord):
    """
    Represents a single facility's emissions data record.

    Attributes:
        npri_id (str): NPRI identifier for the facility.
        facility_name (str): Name of the facility.
        company (str): Company operating the facility.
        address (str): Street address of the facility.
        city (str): City where the facility is located.
        province (str): Province or territory of the facility.
        postal_code (str): Postal code of the facility.
        latitude (str): Latitude coordinate.
        longitude (str): Longitude coordinate.
        emissions (str): Reported emissions value.
        units (str): Units of emissions (e.g., kg).
        facility_details (str): Additional facility details.
        facility_info (str): Supplementary facility information.
        report_year (str): The reporting year of the emissions data.
    """

    def __init__(self, 
                 npri_id, facility_name, company, address, city, province,
                 postal_code, latitude, longitude, emissions, units,
                 facility_details, facility_info, report_year):
        """
        Initializes a new instance of DataRecord with all required fields.
        """
        self.npri_id = npri_id
        self.facility_name = facility_name
        self.company = company
        self.address = address
        self.city = city
        self.province = province
        self.postal_code = postal_code
        self.latitude = latitude
        self.longitude = longitude
        self.emissions = emissions
        self.units = units
        self.facility_details = facility_details
        self.facility_info = facility_info
        self.report_year = report_year

    def __str__(self):
        """
        Returns a human-readable summary of the data record.
        """
        return f"{self.facility_name} ({self.company}) - {self.city}, {self.province} | {self.emissions} {self.units}"

    def to_csv_row(self):
        """
        Converts the data record into a single CSV-formatted string.
        """
        return f"{self.npri_id},{self.facility_name},{self.company},{self.address},{self.city},{self.province},{self.postal_code},{self.latitude},{self.longitude},{self.emissions},{self.units},{self.facility_details},{self.facility_info},{self.report_year}"

    def display(self):
        """
        Displays the record in a basic format (polymorphic method).
        """
        print(str(self))