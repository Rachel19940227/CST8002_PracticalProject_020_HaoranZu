"""
Course: CST8002 Programming Language Research Project
Professor: Tyler DeLa
Due Date: 2025-07-13
Author: Haoran Zu
Description: Part of solution for Practical Project 3
"""

from PersistenceLayer.repository import DataRepository

class DataManager:
    """
    Manages in-memory data operations.
    Acts as an intermediary between the controller and the data repository.
    """

    def __init__(self):
        """
        Initializes the DataManager with a DataRepository.
        Loads data from a predefined CSV file.
        """
        self.repo = DataRepository()  # Instantiate the repository
        self.data_file = "data/Nitrogen oxide emissions by facility.csv"
        self.reload_data()

    def reload_data(self):
        """
        Reloads data from the CSV file using the repository.
        Stores the loaded data in memory.
        """
        self.repo.read_data_records(self.data_file)
        self.data = self.repo.get_all()  # Assign loaded data to memory

    def get_all(self):
        """
        Returns all records currently stored in memory.

        Returns:
            list: All data records.
        """
        return self.data

    def get_by_index(self, index):
        """
        Returns a single record at the given index.

        Args:
            index (int): Index of the desired record.

        Returns:
            DataRecord or None: The record if index is valid, otherwise None.
        """
        if 0 <= index < len(self.data):
            return self.data[index]
        return None

    def add_record(self, record):
        """
        Adds a new record to the in-memory list.

        Args:
            record (DataRecord): The record to add.
        """
        self.data.append(record)

    def update_record(self, index, new_record):
        """
        Updates an existing record at the given index.

        Args:
            index (int): Index of the record to update.
            new_record (DataRecord): The new data to replace the old one.

        Returns:
            bool: True if update is successful, False if index is invalid.
        """
        if 0 <= index < len(self.data):
            self.data[index] = new_record
            return True
        return False

    def delete_record(self, index):
        """
        Deletes a record at the given index.

        Args:
            index (int): Index of the record to delete.

        Returns:
            bool: True if deletion is successful, False if index is invalid.
        """
        if 0 <= index < len(self.data):
            del self.data[index]
            return True
        return False

    def sort_records(self, key_field: str, reverse: bool = False):
        """
        Sorts the in-memory list of records (List) by the given field using Python's list sort.

        Args:
            key_field (str): The attribute name to sort by.
            reverse (bool): Sort descending if True, ascending if False.

        Returns:
            list: The sorted list of DataRecord objects.
        """
        try:
            self.data.sort(key=lambda r: getattr(r, key_field), reverse=reverse)
        except AttributeError:
            print(f"[Error] Invalid field name: '{key_field}'")
        return self.data

    def sort_records_multiple(self, key):
        return sorted(self.data, key=key)

