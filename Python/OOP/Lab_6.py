## add abstract classes

class Salary:
	def __init__(self.pay,reward):
		self.pay = pay
		self.reward = reward

	def anual_salary(self):
		return(self.pay*12)+self.reward

class Employee:
	def __init__(self, name, position, sal):
		self.name = name
		self.position=position
		self.final_salary = sal

	def final_salary(self):
		return self.final_salary.anual_salary()

emap = Employee("Shubman", "Py Dev",sal)
print(emp.final_salary())