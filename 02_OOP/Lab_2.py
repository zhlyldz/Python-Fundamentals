
# Kalıtım (Inheritance)

# Pyton 2.0 kadar bir sınıf yaratıldığında onun object sınıfından kalıtım alması zorunlunyu. 3 versiyonundan sonra bu durum değişti ve artık bir sınıf yaratırken object yazmıyoruz.
# region
# class Person:
# 	age = 0
#
# 	def __init__(self, first_name: str, last_name:str):
# 		self.last_name = last_name
# 		self.first_name = first_name
# 		print('A person has been created..!')
#
# 	def get_full_name(self) -> str:
# 		return self.first_name + ' ' + self.last_name
#
# 	def get_meta_info(self) -> list:
# 		return dir(Person)
#
#
# person_1 = Person('Burak', 'Yılmaz')
# person_1.age = 34
# print(person_1.get_full_name())
# print(person_1.get_meta_info())
#
#
# # Employee sınıfı Person sınıfından kalıtım aldığı içiin Person sınıfın sahip olduğu tüm özelliklere sahiptir.
# class Employee(Person):
# 	pass
#
#
# e1 = Employee('Hakan', 'Yılmaz')
# e1.age = 37
# print(e1.get_full_name())
# print(e1.get_meta_info())
# endregion

# region
# BaseEntity adından bir ata sınıf oluşturun
# Bu sınıfın Id, first_name, last_name, salary, department, create_date, status gibi object attribute olsun
# status attribute Enum tipinde olacak. Active=1, Modified=2, Passive=3

# Employee sınıfımız olsun. BaseEntity kalıtım alacak

# Human_Resource sınıfımız olsun. BaseEntity kalıtım alacak
# create_employee, update_employee, read_employee, delete_employee

# Employee'Ler listede tutulsun.
# endregion

from enum import Enum
from datetime import datetime
from uuid import uuid4

employees = []


class Status(Enum):
	Active = 1
	Modified = 2
	Passive = 3
	
	
class BaseEntiy:
	def __init__(self, first_name, last_name, create_date, status, salary, department):
		self.department = department
		self.salary = salary
		self.status = status
		self.create_date = create_date
		self.last_name = last_name
		self.first_name = first_name
		self.id = uuid4()
		
		
class Employee(BaseEntiy):
	pass


class Human_Resource(BaseEntiy):
	def create_employee(self, employee: Employee) -> None:
		employees.append(employee)
		print('Employee has been created!')
	
	def take_info_create_employee(self, first_name, last_name, create_date, status, salary, department) -> Employee:
		return Employee(first_name, last_name, create_date, status, salary, department)
	
	def get_all_employee(self) -> None:
		for employee in employees:
			if employee.status != Status.Passive:
				print(f"Id: {employee.id}\n"
				      f"First Name: {employee.first_name}\n"
				      f"Last Name: {employee.last_name}\n"
				      f"Department: {employee.department}\n"
				      f"Salary: {employee.salary}\n"
				      f"Create Date: {employee.create_date}\n"
				      f"Status: {employee.status}")
	
	def get_employee_by_full_name(self, full_name: str):
		for employee in employees:
			if f'{employee.first_name} {employee.last_name}'.__contains__(full_name):
				print(f"Id: {employee.id}\n"
				      f"First Name: {employee.first_name}\n"
				      f"Last Name: {employee.last_name}\n"
				      f"Department: {employee.department}\n"
				      f"Salary: {employee.salary}\n"
				      f"Create Date: {employee.create_date}\n"
				      f"Status: {employee.status}")
				
	def get_employee_by_id(self, id: str):
		for employee in employees:
			if employee.id == id:
				return employee
			
	def update_employee(self, employee_arg: Employee, first_name: str,  last_name: str, salary: int, department: str):
		for employee in employees:
			if employee.id == employee_arg.id:
				if first_name != ' ':
					employee.first_name = first_name
				if last_name != ' ':
					employee.last_name = last_name
				if salary != ' ':
					employee.salary = salary
				if department != ' ':
					employee.department = department
		
				employee.status = Status.Modified
				
	def delete_employee(self, id):
		for employee in employees:
			if employee.id == id:
				employee.status = Status.Passive
	
	
def main():
	hr_1 = Human_Resource('İpek', 'Yılmaz', datetime.now(), Status.Active, 1000, 'HR')
	
	while True:
		process = input('Create Employee           ==> 1\n'
		                'List of Employees         ==> 2\n'
		                'Get Employee By Full Name ==> 3\n'
		                'Update Employee           ==> 4\n'
		                'Delete Employee           ==> 5\n'
		                'Exit                      ==> 6\n'
		                'Please choose a process: ')
	
		if process == '1':
			first_name = input('First Name: ')
			last_name = input('Last Name: ')
			department = input('Department: ')
			salary = input('Salary: ')
	
			new_employee = hr_1.take_info_create_employee(
				first_name, last_name, datetime.now(), Status.Active, department, salary
			)
			
			hr_1.create_employee(new_employee)
		elif process == '2':
			hr_1.get_all_employee()
		elif process == '3':
			full_name = input('Please type into full name: ')
			hr_1.get_employee_by_full_name(full_name)
		elif process == '4':
			employee_id = input('Id: ')
			employee = hr_1.get_employee_by_id(employee_id)
			hr_1.update_employee(employee, "", "", 2000, "ARGE")
		elif process == '5':
			employee_id = input('Id: ')
			hr_1.delete_employee(employee_id)
			
		
main()