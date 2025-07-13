"""
Course: CST8002 Programming Language Research Project
Professor: Tyler DeLa
Due Date: 2025-07-13
Author: Haoran Zu
Description: Part of solution for Practical Project 3
"""

import unittest
from BusinessLayer.data_manager import DataManager
from PersistenceLayer.data_record import DataRecord

class TestDataManagerSorting(unittest.TestCase):
    def setUp(self):
        """
        This method runs before each test.
        It initializes a DataManager instance and populates it with sample DataRecord entries
        to test sorting functionality.
        """
        self.manager = DataManager()
        self.manager.data = [
            DataRecord(
                npri_id="1",
                company="Company A",
                address="123 Main St",
                city="Ottawa",
                province="ON",
                postal_code="K1A0B1",
                latitude=45.4215,
                longitude=-75.6972,
                units="kg",
                facility_details="Details A",
                facility_info="Info A",
                report_year=2022,
                emissions=50.0,
                facility_name="Zeta Plant"  # Should appear second in ascending sort
            ),
            DataRecord(
                npri_id="2",
                company="Company B",
                address="456 Second St",
                city="Toronto",
                province="ON",
                postal_code="M5H2N2",
                latitude=43.6532,
                longitude=-79.3832,
                units="kg",
                facility_details="Details B",
                facility_info="Info B",
                report_year=2022,
                emissions=70.0,
                facility_name="Alpha Plant"  # Should appear first in ascending sort
            )
        ]

    def test_sort_by_facility_name_ascending(self):
        """
        Test sorting the data by 'facility_name' in ascending order.
        Expected order: 'Alpha Plant' should come before 'Zeta Plant'.
        """
        sorted_data = self.manager.sort_records("facility_name", reverse=False)
        facility_names = [record.facility_name for record in sorted_data]
        self.assertEqual(facility_names, ["Alpha Plant", "Zeta Plant"])

# Run the tests if this file is executed directly
if __name__ == "__main__":
    unittest.main()