# generate_data.py - creates synthetic payroll history for analysis
# Run once:  python generate_data.py
# Output:    data/payroll_history.csv
# Size:      25 employees x 4 years x 12 months = 1200 rows

import csv
import os
import random

random.seed(42)  # fixed seed => same data every run (reproducible)

BASE_WAGE_PER_HOUR = 20
ANNUAL_RAISE = 0.05  # 5% raise each year
START_YEAR = 2023
OUTPUT_PATH = "data/payroll_history.csv"

DEPARTMENTS = ["Engineering", "Sales", "HR", "Marketing", "Finance"]
YEARS = [2023, 2024, 2025, 2026]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

FIRST_NAMES = [
    "abhinav", "joe", "ram", "sara", "neha", "arjun", "priya", "vikram",
    "anjali", "rahul", "divya", "karan", "meera", "rohit", "sneha",
    "aditya", "pooja", "sanjay", "kavya", "manoj", "ritu", "deepak",
    "nisha", "varun", "swati",
]


def hourly_rate_for_year(year):
    """Wage per hour grows 5% each year from the start year."""
    years_elapsed = year - START_YEAR
    rate = BASE_WAGE_PER_HOUR * ((1 + ANNUAL_RAISE) ** years_elapsed)
    return round(rate, 2)


def build_employees():
    """Assign each employee a fixed department."""
    employees = []
    for emp_id, name in enumerate(FIRST_NAMES, start=1):
        employees.append({
            "emp_id": emp_id,
            "name": name,
            "department": random.choice(DEPARTMENTS),
        })
    return employees


def generate_rows(employees):
    """One row per employee per year per month."""
    rows = []
    for emp in employees:
        for year in YEARS:
            rate = hourly_rate_for_year(year)
            for month in MONTHS:
                leaves = random.randint(0, 5)
                days_worked = 20 - leaves
                # mix of full (8h) and half (4h) days
                full_days = random.randint(0, days_worked)
                half_days = days_worked - full_days
                hours_worked = full_days * 8 + half_days * 4
                wage = round(hours_worked * rate, 2)

                rows.append({
                    "emp_id": emp["emp_id"],
                    "name": emp["name"],
                    "department": emp["department"],
                    "year": year,
                    "month": month,
                    "leaves": leaves,
                    "days_worked": days_worked,
                    "hours_worked": hours_worked,
                    "hourly_rate": rate,
                    "wage": wage,
                })
    return rows


def main():
    os.makedirs("data", exist_ok=True)
    employees = build_employees()
    rows = generate_rows(employees)

    fieldnames = ["emp_id", "name", "department", "year", "month",
                  "leaves", "days_worked", "hours_worked", "hourly_rate", "wage"]

    with open(OUTPUT_PATH, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} payroll records -> {OUTPUT_PATH}")
    print(f"{len(employees)} employees x {len(YEARS)} years x {len(MONTHS)} months")


if __name__ == "__main__":
    main()
