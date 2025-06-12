"""
Course: CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 2025-06-15
Author: Haoran Zu
Description: Part of solution for Practical Project 2
"""
import csv
from PersistenceLayer.data_record import DataRecord
from BusinessLayer.data_controller import DataController


if __name__ == "__main__":
    # Instantiate and run the application controller
    app = DataController()
    app.run()
