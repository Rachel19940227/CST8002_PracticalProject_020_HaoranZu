import unittest
from BusinessLayer.data_manager import DataManager
from PersistenceLayer.data_record import DataRecord

class TestDataManagerSorting(unittest.TestCase):
    def setUp(self):
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
                facility_name="Zeta Plant"
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
                facility_name="Alpha Plant"
            )
        ]

    def test_sort_by_facility_name_ascending(self):
        sorted_data = self.manager.sort_records("facility_name", reverse=False)
        facility_names = [record.facility_name for record in sorted_data]
        self.assertEqual(facility_names, ["Alpha Plant", "Zeta Plant"])

if __name__ == "__main__":
    unittest.main()
