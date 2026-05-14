# MAIN.PY - EMPLOYEE WAGE CALCULATOR
import random 

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_DAY_HOURS = 4
MAX_WORKING_DAYS = 20
MAX_WORKING_HOURS = 100



def check_attendance():
    attendance = random.randint(0,2)
    return attendance 

def calculate_daily_wage(attendance):
    # 1= FULL,2=HALF,0 = ABSENT
    if attendance ==1:
        return WAGE_PER_HOUR*FULL_DAY_HOURS
    elif attendance ==2:
        return WAGE_PER_HOUR* PART_DAY_HOURS
    else:
        return 0 
    

def calculate_monthly_wage(employee_name):
    total_wage = 0
    total_days = 0
    total_hours = 0

    while total_days<MAX_WORKING_DAYS and total_hours<MAX_WORKING_HOURS:
        attendance = check_attendance()
        daily_wage = calculate_daily_wage(attendance)

        if attendance == 1:
            total_hours += FULL_DAY_HOURS
            total_days  += 1
        elif attendance == 2:
            total_hours += PART_DAY_HOURS
            total_days  += 1

        total_wage += daily_wage

    print(f"\n{'='*40}")
    print(f"Employee  : {employee_name}")
    print(f"Total Days Worked : {total_days}")
    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Monthly Wage: ${total_wage}")
    print(f"{'='*40}")

    return{
        "name": employee_name,
        "days": total_days,
        "hours": total_hours,
        "wage": total_wage

    }


def main():
    print("=== EMPLOYEE PAYROLL SYSTEM ===")
    print("1. Calculate wage for one employee")
    print("2. Calculate wages for multiple employees")
    print("3. Exit")

    choice = input("\nEnter choice: ")


    if choice == "1":
        name = input ("enter employee name ")
        calculate_monthly_wage(name)

    elif choice == "2" :
        n = int (input("how many employees" ))
        employees = []
        for i in range (n):
            name = input (f"enter the name of employee {i+1}:")
            result = calculate_monthly_wage
            employees.append(result)

        print("\n=== SUMMARY ===")
        for emp in employees:
            print(f"{emp['name']}: ${emp['wage']}")

    elif choice == "3":
        print("good bye !")

if __name__ == "__main__":
    main()