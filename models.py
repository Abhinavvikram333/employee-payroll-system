import random 
from employee_data import save_employee

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_DAY_HOURS = 4
MAX_WORKING_DAYS = 20
MAX_WORKING_HOURS = 100


class Employee:
    def __init__(self,name):
        self.name=name
        self.total_days= 0 
        self.total_hours = 0 
        self.total_wage = 0 

    def check_attendance(self):
        # 0 -absent,1 full ,2 half day
        return random.randint(0,2)
    
    def calculate_daily_wage(self,attendance):
        if attendance == 1:
            return WAGE_PER_HOUR* FULL_DAY_HOURS
        elif attendance == 2 :
            return WAGE_PER_HOUR* PART_DAY_HOURS
        else :
            return 0 
        
    def calculate_monthly_wage(self):
        while self.total_days< MAX_WORKING_DAYS and self.total_hours<MAX_WORKING_HOURS :
            attendance = self.check_attendance()
            daily_wage = self. calculate_daily_wage(attendance)

            if attendance == 1:
                self.total_hours += FULL_DAY_HOURS
                self.total_days += 1
            elif attendance == 2 :
                self.total_hours += PART_DAY_HOURS
                self.total_days += 1


            self.total_wage += daily_wage

    
    def to_dict(self):

        return {
            "name":self.name,
            "days":self.total_days,
            "hours":self.total_hours,
            "wage" : self.total_wage,
        }
    
    def show_summary(self):
        print(f"\n{'='*40}")
        print(f"Employee  : {self.name}")
        print(f"Total Days Worked : {self.total_days}")
        print(f"Total Hours Worked: {self.total_hours}")
        print(f"Total Monthly Wage: ${self.total_wage}")
        print(f"{'='*40}")

class PayrollManager:
    """runs pay roll for 1 or many more employees"""

    def __init__(self):
        self.employees = []

    def run_payroll(self, name):
        employee = Employee (name)
        employee.calculate_monthly_wage()
        employee.show_summary()
        save_employee(employee.to_dict())
        self.employees.append(employee)
        return employee
    
    def show_summary(self):
        print("\n=== SUMMARY ===")
        for emp in self.employees:
            print(f"{emp.name} : $ {emp.total_wage}")