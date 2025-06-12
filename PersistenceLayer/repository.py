"""
Course: CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 2025-06-15
Author: Haoran Zu
Description: Part of solution for Practical Project 2
"""

import csv
import uuid
from .data_record import DataRecord

class DataRepository:
    """
    Handles data persistence operations such as reading from and writing to files.
    Maintains an in-memory list of DataRecord objects.
    """

    def __init__(self):
        """
        Initializes the repository with an empty list of records.
        """
        self.records = []

    def read_data_records(self, filename):
        """
        Reads up to 100 data records from a CSV file and loads them into memory.

        Args:
            filename (str): Path to the CSV file.
        """
        self.records = []
        try:
            with open(filename, mode='r', encoding='windows-1252') as file:
                reader = csv.DictReader(file)
                for i, row in enumerate(reader):
                    if i >= 100:
                        break
                    record = DataRecord(
                        npri_id=row["NPRI ID"],
                        facility_name=row["Facility name"],
                        company=row["Company name"],
                        address=row["Address"],
                        city=row["City"],
                        province=row["Province"],
                        postal_code=row["PostalCode"],
                        latitude=row["Latitude"],
                        longitude=row["Longitude"],
                        emissions=row["Emissions"],
                        units=row["Units"],
                        facility_details=row["Facility details"],
                        facility_info=row["Facility information"],
                        report_year=row["Report year"]
                    )
                    self.records.append(record)
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_to_file(self):
        """
        Saves the current records to a new CSV file with a unique name.

        Returns:
            str: The generated filename where records were saved.
        """
        filename = f"data_{uuid.uuid4()}.csv"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("NPRI ID,Facility name,Company name,Address,City,Province,PostalCode,"
                    "Latitude,Longitude,Emissions,Units,Facility details,Facility information,"
                    "Report year\n")
            for record in self.records:
                f.write(record.to_csv_row() + "\n")
        return filename

    def get_all(self):
        """
        Returns all records currently in memory.

        Returns:
            list: A list of DataRecord objects.
        """
        return self.records

    def get_by_index(self, index: int):
        """
        Retrieves a record by its index.

        Args:
            index (int): Index of the desired record.

        Returns:
            DataRecord or None: The record if found, otherwise None.
        """
        if 0 <= index < len(self.records):
            return self.records[index]
        return None

    def add_record(self, record: DataRecord):
        """
        Adds a new DataRecord to the repository.

        Args:
            record (DataRecord): The record to add.
        """
        self.records.append(record)

    def update_record(self, index: int, new_record: DataRecord):
        """
        Updates a record at the specified index.

        Args:
            index (int): The index of the record to update.
            new_record (DataRecord): The updated record.

        Returns:
            bool: True if update is successful, False if index is invalid.
        """
        if 0 <= index < len(self.records):
            self.records[index] = new_record
            return True
        return False

    def delete_record(self, index: int):
        """
        Deletes a record at the specified index.

        Args:
            index (int): The index of the record to delete.

        Returns:
            bool: True if deletion is successful, False if index is invalid.
        """
        if 0 <= index < len(self.records):
            del self.records[index]
            return True
        return False
