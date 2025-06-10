"""
Course: CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: 2025-05-25
Author: Haoran Zu
"""
import csv
from Model.data_record import DataRecord

def read_data_records(filename):
    #Reads emission data from a CSV file and converts rows into DataRecord objects.
    records = []
    try:
        with open(filename, mode='r', encoding='windows-1252') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
                if i >= 100:  # 只加载前100行作为样例
                    break
                #Create a DataRecord instance using values from the current row
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
                records.append(record)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return records

def main():
    #Main function to read data records and print them
    print("Haoran Zu - Practice Project - 02\n" + "-"*50)
    data_file = "D:/AC-CP/Level4/programming language/Assignment/Nitrogen oxide emissions by facility.csv"
    facilities = read_data_records(data_file)
    for record in facilities:
        print(record)

if __name__ == "__main__":
    main()
# This code is a simple Python script that reads a CSV file containing data about nitrogen oxide emissions by facility.