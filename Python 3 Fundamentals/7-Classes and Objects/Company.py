from Employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:

  def __init__(self):
    self.employees = []

  def addEmployee(self, employee):
    self.employees.append(employee)

  def payEmployees(self):
    for e in self.employees:
      print("Paying:",e.fname,e.lname)
      print(f"Amount: $ {e.calculatePaycheck():,.2f}")
      print("---------------")

def main():
  
  myCompany = Company()

  employee1 = SalaryEmployee("Edgar","Itzak",100000)
  employee2 = CommissionEmployee("Jose", "Ruiz", 200000, 50, 10)
  employee3 = HourlyEmployee("Sarah", "Hess", 25, 50)

  myCompany.addEmployee(employee1)
  myCompany.addEmployee(employee2)
  myCompany.addEmployee(employee3)

  myCompany.payEmployees()

main()

