
from models import PayrollManager
from employee_data import display_all_employees

def main():
    payroll = PayrollManager()

    print("=== EMPLOYEE PAYROLL SYSTEM ===")
    print("1. Calculate wage for one employee")
    print("2. Calculate wages for multiple employees")
    print("3. Exit")
    print("4. View all saved employees")

    choice = input("\nEnter choice: ")

    if choice == "1":
        name = input ("enter employee name ")
        payroll.run_payroll(name)

    elif choice == "2":
        n = int(input("how many employees?"))
        for i in range (n):
            name = input(f"enter the name of employee {i+1} : ")
            payroll.run_payroll(name)
        payroll.show_summary()

    elif choice == "3":
        print("good bye ! ")

    elif choice == "4":
        display_all_employees()


if __name__ == "__main__":
    main()