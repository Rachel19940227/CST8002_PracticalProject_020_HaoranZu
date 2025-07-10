"""
Course: CST8002 Programming Language Research Project
Professor: Tyler DeLa
Due Date: 2025-07-13
Author: Haoran Zu
Description: Part of solution for Practical Project 3
"""

from PersistenceLayer.data_record import DataRecord
from rich.console import Console
from rich.table import Table

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
        print("9. Sort by which field")

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
        Displays all DataRecord (or BaseRecord) objects from a list in a formatted table.
        I change the sorting method that just show 4 coloums to make it easier to read.

        Args:
            records (list): A list of DataRecord or BaseRecord instances.
        """
        console = Console()
        table = Table(title="Emission Records - Haoran Zu")

        table.add_column("Index", style="dim", width=6)
        table.add_column("Facility", style="cyan", no_wrap=True)
        table.add_column("Company", style="magenta")
        table.add_column("City", style="green")
        table.add_column("Emissions", style="yellow")

        for i, r in enumerate(records):
            # Try to display important fields; fallback to string if attribute missing
            try:
                facility = getattr(r, "facility_name", str(r))
                company = getattr(r, "company", "N/A")
                city = getattr(r, "city", "N/A")
                emissions = getattr(r, "emissions", "N/A")
            except Exception:
                facility = company = city = emissions = "Error"

            table.add_row(str(i), facility, company, city, emissions)

        console.print(table)

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
