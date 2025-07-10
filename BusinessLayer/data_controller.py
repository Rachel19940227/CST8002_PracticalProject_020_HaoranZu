"""
Course: CST8002 Programming Language Research Project
Professor: Tyler DeLa
Due Date: 2025-07-13
Author: Haoran Zu
Description: Part of solution for Practical Project 3
"""




from BusinessLayer.data_manager import DataManager
from PersistenceLayer.data_record import DataRecord

from PresentationLayer.view import ConsoleView
from PersistenceLayer.data_record import DataRecord

class DataController:
    """
    Acts as the controller in the architecture.
    Handles user input and delegates actions to the DataManager and View.
    """

    def __init__(self):
        """
        Initializes the DataController with a DataManager instance.
        """
        self.manager = DataManager()

    def run(self):
        """
        Main loop to display the menu and handle user choices.
        Supports actions such as reloading data, viewing records, 
        adding/updating/deleting records, and saving to a file.
        """
        while True:
            ConsoleView.display_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                # Reloads data from the source
                self.manager.reload_data()
                ConsoleView.show_message("Reload successful.")

            elif choice == "2":
                # Saves current data to a new file with UUID name
                filename = self.manager.repo.save_to_file()
                print(f"Data saved to {filename}")

            elif choice == "3":
                # Displays all records from 1-100
                ConsoleView.show_all(self.manager.get_all())

            elif choice == "4":
                # Displays a single record by index
                index = int(input("Enter record index (0-based): "))
                record = self.manager.get_by_index(index)
                if record:
                    ConsoleView.show_record(record)
                else:
                    ConsoleView.show_message("Invalid index.")

            elif choice == "5":
                # Adds a new record using user input, I choose some of the info, not all
                name = input("Facility name: ").strip()
                company = input("Company name: ").strip()
                address = input("Address: ").strip()
                city = input("City: ").strip()
                province = input("Province: ").strip()

                new_record = DataRecord(
                    npri_id="",  
                    facility_name=name,
                    company=company,
                    address=address,
                    city=city,
                    province=province,
                    postal_code="", latitude="", longitude="",
                    emissions="0", units="kg",
                    facility_details="", facility_info="",
                    report_year="2023"
                )
                self.manager.add_record(new_record)
                ConsoleView.show_message("Record added.")

            elif choice == "6":
                # Updates an existing record by index, index from 0-99
                try:
                    index = int(input("Enter record index to update: "))
                    existing = self.manager.get_by_index(index)
                    if existing:
                        print("Leave blank to keep existing value.")
                        name = input(f"New Facility name (current: {existing.facility_name}): ").strip()
                        company = input(f"New Company name (current: {existing.company}): ").strip()
                        address = input(f"New Address (current: {existing.address}): ").strip()
                        city = input(f"New City (current: {existing.city}): ").strip()
                        province = input(f"New Province (current: {existing.province}): ").strip()

                        updated = DataRecord(
                            npri_id=existing.npri_id,
                            facility_name=name or existing.facility_name,
                            company=company or existing.company,
                            address=address or existing.address,
                            city=city or existing.city,
                            province=province or existing.province,
                            postal_code=existing.postal_code,
                            latitude=existing.latitude,
                            longitude=existing.longitude,
                            emissions=existing.emissions,
                            units=existing.units,
                            facility_details=existing.facility_details,
                            facility_info=existing.facility_info,
                            report_year=existing.report_year
                        )
                        self.manager.update_record(index, updated)
                        ConsoleView.show_message("Record updated.")
                    else:
                        ConsoleView.show_message("Invalid index.")
                except ValueError:
                    ConsoleView.show_message("Please enter a valid number.")

            elif choice == "7":
                # Deletes a record by index, from the simple data structure in memory
                index = int(input("Enter record index to delete: "))
                if self.manager.delete_record(index):
                    ConsoleView.show_message("Deleted.")
                else:
                    ConsoleView.show_message("Invalid index.")

            elif choice == "8":
                # Exits the application
                ConsoleView.show_message("Goodbye!")
                break

            elif choice == "9":
                print("Sort records by:")
                print("1. Facility Name")
                print("2. Company Name")
                print("3. City")
                print("4. Emissions")
                choice = input("Choose a field (1-4): ").strip()

                sort_field_map = {
                    "1": "facility_name",
                    "2": "company",
                    "3": "city",
                    "4": "emissions"
                }

                key_field = sort_field_map.get(choice)

                if key_field:
                    sorted_list = self.manager.sort_records(key_field=key_field)
                    ConsoleView.show_all(sorted_list)
                else:
                    ConsoleView.show_message("Invalid choice. No sorting performed.")


            else:
                ConsoleView.show_message("Invalid option.")
