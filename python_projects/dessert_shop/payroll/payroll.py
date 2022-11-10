"""payroll.py"""
from abc import ABC, abstractmethod
import csv
import os

PAY_LOGFILE = 'paylog.txt'
employees = []

class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification
    
    def make_hourly(self, hourly_rate):
        self.classification = Hourly(hourly_rate)
    
    def make_salaried(self, salary):
        self.classification = Salary(salary)

    def make_commissioned(self, salary, commission):
        self.classification = Commissioned(salary, commission)

    def initiate_payment(self):
        self.classification.compute_pay()

    def issue_payment(self):
        self.classification.issue_payment()

class Classification(ABC):
    def issue_payment(self):
        with open(PAY_LOGFILE, "w", encoding="utf-8") as file:
            for emp in employees:
                file.write(f"Mailing ${emp.classification.compute_pay()} to {emp.first_name} {emp.last_name} at {emp.address}, {emp.city}, {emp.state}, {emp.zipcode}\n")
        file.close()
        self.reset()

    @abstractmethod
    def compute_pay(self):
        pass

    def reset(self):
        for emp in employees:
            if emp.classification == '2':
                emp.classification.receipts = ["0"]
            elif emp.classification == '3':
                emp.classification.timecard = ["0"]

class Hourly(Classification):

    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecard = ["0"]

    def compute_pay(self):
        pay = 0
        for hours in self.timecard:
            pay += (float(hours) * float(self.hourly_rate))
        pay = f"{'{:.2f}'.format(pay)}"
        return pay

    def add_timecard(self, timecard):
        if type(timecard) == float:
            self.timecard.append(timecard)
        else:
            self.timecard = timecard

    def __str__(self):
        return f"Hourly: {self.timecard}"

class Salary(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        pay = float(self.salary) * (1/24)
        pay = f"{'{:.2f}'.format(pay)}"
        return pay

    def __str__(self):
        return "Salary"

class Commissioned(Salary):

    def __init__(self, salary, commission_rate):
        super().__init__(float(salary))
        self.commission_rate = float(commission_rate) / 100
        self.receipts = ["0"]

    def compute_pay(self):
        pay = float(self.salary) * (1/24)
        for receipt in self.receipts:
            pay += self.commission_rate * float(receipt)
        pay = f"{'{:.2f}'.format(pay)}"
        return pay

    def add_receipt(self, receipts):
        if type(receipts) == float:
            self.receipts.append(receipts)
        else:
            self.receipts = receipts

    def __str__(self):
        return "Commissioned"

def load_employees():
    with open('employees.csv', 'r', encoding="utf-8") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            employee_obj = Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            if employee_obj.classification == '3':
                employee_obj.make_hourly(row[10])
            elif employee_obj.classification == '1':
                employee_obj.make_salaried(row[8])
            elif employee_obj.classification == '2':
                employee_obj.make_commissioned(row[8], row[9])
            employees.append(employee_obj)
    file.close()

def find_employee_by_id(emp_id: str):
    for employee in employees:
        if employee.emp_id == emp_id:
            return employee

def process_timecards():
    with open("timecards.csv", "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            for employee in employees:
                if employee.emp_id == row[0]:
                    row.pop(0)
                    Hourly.add_timecard(employee.classification, row)
        file.close()

def process_receipts():
    with open("receipts.csv", "r", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            for employee in employees:
                if employee.emp_id == row[0]:
                    row.pop(0)
                    Commissioned.add_receipt(employee.classification, row)
        file.close()

def run_payroll():
    if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘payroll.txt’
        os.remove(PAY_LOGFILE)
    for emp in employees: # employees is the global list of Employee objects
        emp.issue_payment() # issue_payment calls a method in the classification
    # object to compute the pay

def main():
    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()

if __name__ == "__main__":
    main()
