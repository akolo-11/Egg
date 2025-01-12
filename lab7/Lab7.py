from time import sleep

class Employee:
    def __init__(self, name, id_number, sex, **kwargs):
        self.name = name
        self.id = id_number
        self.sex = sex
    def get_info(self):
        return f"{self.id} | {self.name} - {self.sex}"

class Manager(Employee):
    def __init__(self, name, id_number, sex, department, *args, **kwargs):
        super().__init__(name, id_number, sex, department=department, **kwargs)# forwards all unused
        self.department = department
    def yell(self, target_employee:Employee):
        print(f"Get to work, {target_employee.name}!")
    def manage_project(self):
        print("Get to work, everyone!")
    def get_info(self):
        return f"{super().get_info()} - manager"

class Technician(Employee):
    def __init__(self, name, id_number, sex, spec, *args, **kwargs):
        super().__init__(name, id_number, sex, spec=spec, **kwargs)# forwards all unused
        if spec != None:
            self.specialization = spec
        else:
            spec = kwargs['spec']
    def perform_maintenance(self):
        sleep(2)
        print(f"{self.get_info()} did some maintenance")
    def get_info(self):
        return f"{super().get_info()} - technician"

class TechManager(Manager, Technician):
    def __init__(self, name, id_number, sex, department, spec):
        super().__init__(name= name, id_number= id_number, sex= sex, department= department, spec= spec)
        self.employees = []
    def add_employee(self, employee:Employee):
        self.employees.append(employee)
    def manage_project(self):
        for employee in self.employees:
            self.yell(employee)
    def get_team_info(self):
        return '\n'.join([employee.get_info() for employee in self.employees])
    def get_info(self):
        return f"{Employee.get_info(self)} - tech manager - {self.department} {self.specialization}"

admin = TechManager("Alice", "1", "female", "IT", "PM")
sysadmin = Technician("Bob", "2", "male", "sysadmin")
manager = Manager("Charlie", "3", "male", "IT")
generic_joe = Employee("Deacon", "4", "male")
generic_mary = Employee("Eve", "5", "female")
generic_joe2 = Employee("Frank", "6", "male")
admin.add_employee(sysadmin)
admin.add_employee(manager)
admin.add_employee(generic_joe)
admin.add_employee(generic_mary)
admin.add_employee(generic_joe2)
print(admin.get_info())
print("------------------")
print(admin.get_team_info())
print("------------------")
sysadmin.__class__ = Employee
print(admin.get_team_info())
print("------------------")
admin.manage_project()
print("------------------")
admin.perform_maintenance()

