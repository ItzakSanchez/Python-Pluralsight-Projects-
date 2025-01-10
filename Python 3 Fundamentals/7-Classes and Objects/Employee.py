class Employee:

  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
  

  
class SalaryEmployee(Employee):
  def __init__(self, fname, lname, salary):
    super().__init__(fname, lname)
    self.salary = salary

  def calculatePaycheck(self):
    return self.salary/52
  
class HourlyEmployee(Employee):
  def __init__(self, fname, lname, weeklyHours, hourlRate):
    super().__init__(fname,lname)
    self.weeklyHours = weeklyHours
    self.hourlRate = hourlRate
  
  def calculatePaycheck(self):
    return self.weeklyHours*self.hourlRate
  
class CommissionEmployee(SalaryEmployee):
  def __init__(self, fname, lname, salary , numberSales, saleCommission):
    super().__init__(fname, lname, salary)
    self.numberSales = numberSales
    self.saleCommission = saleCommission

  def calculatePaycheck(self):
    regularPay = super().calculatePaycheck()
    commissionPay = self.numberSales*self.saleCommission
    return regularPay+commissionPay