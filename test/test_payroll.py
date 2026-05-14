
from models import Employee

def test_full_day_wage():
    # A full day = 8 hours x $20 = $160
    emp = Employee("tester")
    assert emp.calculate_daily_wage(1) == 160 


def test_half_day_wage():
    # a half day = 4 hours x $20 = $ 160 
    emp = Employee("tester")
    assert emp.calculate_daily_wage(2) == 80 

def test_absent_day_wage():
    #absent = 0 
    emp = Employee("tester")
    assert emp.calculate_daily_wage(0) == 0