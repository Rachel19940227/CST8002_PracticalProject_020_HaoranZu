"""
Course: CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 2025-05-25
Author: Haoran Zu
"""

class DataRecord:
    def __init__(self, 
                 npri_id, facility_name, company, address, city, province,
                 postal_code, latitude, longitude, emissions, units,
                 facility_details, facility_info, report_year):
        """
        Parameters:
            npri_id (str): NPRI identifier for the facility.
            facility_name (str): Name of the facility.
            company (str): Name of the company operating the facility.
            address (str): Street address of the facility.
            city (str): City where the facility is located.
            province (str): Province or territory of the facility.
            postal_code (str): Postal code of the facility.
            latitude (str): Latitude coordinate.
            longitude (str): Longitude coordinate.
            emissions (str): Emission amount.
            units (str): Units for the emission amount.
            facility_details (str): Additional facility details.
            facility_info (str): Facility information.
            report_year (str): The year of the emissions report.
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
        # Returns a string representation of the DataRecord instance.
        return f"{self.facility_name} ({self.company}) - {self.city}, {self.province} | {self.emissions} {self.units}"
