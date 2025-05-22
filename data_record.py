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
        return f"{self.facility_name} ({self.company}) - {self.city}, {self.province} | {self.emissions} {self.units}"
