"""
Course: CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 2025-06-15
Author: Haoran Zu
Description: Part of solution for Practical Project 2
"""


from PersistenceLayer.data_record import DataRecord

class ConsoleView:
    """
    Provides console-based user interface for interacting with the data.
    Includes methods to display menus, records, and user prompts.
    """

    @staticmethod
    def display_menu():
        """
        Displays the main menu options to the console.
        """
        print("=== Program by Haoran Zu ===")
        print("\n1. Reload Data")
        print("2. Save Data to New File")
        print("3. Show All Records")
        print("4. Show One Record")
        print("5. Add New Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Exit")

    @staticmethod
    def show_record(record: DataRecord):
        """
        Prints a single DataRecord to the console.

        Args:
            record (DataRecord): The record to be displayed.
        """
        print(record)

    @staticmethod
    def show_all(records):
        """
        Displays all DataRecord objects from a list.

        Args:
            records (list): A list of DataRecord instances.
        """
        for r in records:
            ConsoleView.show_record(r)

    @staticmethod
    def get_input(prompt: str):
        """
        Prompts the user for input.

        Args:
            prompt (str): The message displayed to the user.

        Returns:
            str: The user's input.
        """
        return input(prompt)

    @staticmethod
    def show_message(message: str):
        """
        Displays a message to the user.

        Args:
            message (str): The message to display.
        """
        print(message)
