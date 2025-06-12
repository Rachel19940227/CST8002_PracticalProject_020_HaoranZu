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
    def test_add_record(self):
        # 准备：实例化 DataManager
        manager = DataManager()
        original_count = len(manager.get_all())

        # 创建一个新的 DataRecord
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

        # 调用 add_record 方法
        manager.add_record(new_record)

        # 断言：数量是否增加
        self.assertEqual(len(manager.get_all()), original_count + 1)

        # 断言：最后一项是否为新添加的记录
        self.assertEqual(manager.get_all()[-1].facility_name, "Test Facility")

if __name__ == '__main__':
    unittest.main()
