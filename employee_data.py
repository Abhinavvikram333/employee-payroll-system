# employee_data.py - Save and Load employees using CSV

import csv
import os

FILE_PATH = "data/employees.csv"

def save_employee(employee: dict):
    """Save a single employee record to CSV"""
    file_exists = os.path.exists(FILE_PATH)

    with open(FILE_PATH, mode='a', newline='') as file:
        fieldnames = ["name", "days", "hours", "wage"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Write header only once

        writer.writerow(employee)
    print(f"✅ Saved {employee['name']} to records.")

def load_all_employees():
    """Load all employee records from CSV"""
    if not os.path.exists(FILE_PATH):
        print("No records found.")
        return []

    with open(FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        employees = [row for row in reader]

    return employees

def display_all_employees():
    """Print all saved employees"""
    employees = load_all_employees()
    if not employees:
        return

    print(f"\n{'='*50}")
    print(f"{'Name':<20} {'Days':<10} {'Hours':<10} {'Wage':<10}")
    print(f"{'='*50}")
    for emp in employees:
        print(f"{emp['name']:<20} {emp['days']:<10} {emp['hours']:<10} ${emp['wage']:<10}")
    print(f"{'='*50}")