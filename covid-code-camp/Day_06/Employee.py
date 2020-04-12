class Employee:
	def __init__ (self, name, ssn, department, salary):
		self.name = name
		self.ssn = ssn
		self.department = department
		self.salary = salary

        def giveRaise(self, amount):
		self.salary = self.salary + amount
		return self.salary

	def payEmployee(self, hours):
		pay = hours * self.salary
		return pay

Bob = Employee("Bob Smith", "000-00-0000", "Accounting", 48)

Mary = Employee("Mary Johnson", "000-00-0000", "Sales", 37)

print(Bob.name + " " + Bob.department)
print(Mary.name + " " + Mary.department)

print("After a raise, Mary's new pay is " + str(Mary.giveRaise(5)) + " dollars per hour.")
print("Mary worked 37 hours, her paycheck is: $" + str(Mary.payEmployee(37)))
print(Bob.name + "worked 31 hours. His paycheck is: $" + str(Bob.payEmployee(31)))
