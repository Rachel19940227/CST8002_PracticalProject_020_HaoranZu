"""
Course: CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 2025-06-15
Author: Haoran Zu
Description: Part of solution for Practical Project 2
"""

import unittest
from BusinessLayer.data_manager import DataManager
from PersistenceLayer.data_record import DataRecord

class TestDataManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Prints header when test class starts"""
        print("\n=== Program by Haoran Zu ===")
        # add my name as input
        
    def test_add_record(self):
        # initialize DataManager
        manager = DataManager()
        original_count = len(manager.get_all())

        # create a new DataRecord
        new_record = DataRecord(
            npri_id="0000001",
            facility_name="Test Facility",
            company="Test Company",
            address="123 Test Street",
            city="Test City",
            province="ON",
            postal_code="A1A1A1",
            latitude="45.4215",
            longitude="-75.6972",
            emissions="123.45",
            units="kg",
            facility_details="Test details",
            facility_info="Info",
            report_year="2023"
        )

        # call add_record method
        manager.add_record(new_record)

        # assert if the record added
        self.assertEqual(len(manager.get_all()), original_count + 1)

        # assert if added the last new record
        self.assertEqual(manager.get_all()[-1].facility_name, "Test Facility")

if __name__ == '__main__':
    unittest.main()