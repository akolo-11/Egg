# Лабораторная работа №7: Работа с классами ч.3

## Описание работы
В данной лабораторной работе рассматриваются продвинутые концепции объектно-ориентированного программирования (ООП) в Python, такие как множественное наследование, инкапсуляция и полиморфизм. Учащиеся разрабатывают систему управления сотрудниками, которая включает различные типы сотрудников: менеджеров, технических специалистов и технических менеджеров. Работа демонстрирует, как комбинировать функциональность нескольких классов с помощью множественного наследования и как использовать полиморфизм для работы с различными типами сотрудников.

## Задание

1. **Создание базового класса `Employee`**:
   - Класс содержит общие атрибуты, такие как `name` (имя) и `id` (идентификационный номер).
   - Метод `get_info()` возвращает базовую информацию о сотруднике.

2. **Создание класса `Manager`**:
   - Наследует от `Employee` и добавляет атрибут `department` (отдел).
   - Метод `manage()` символизирует управление проектами.

3. **Создание класса `Technician`**:
   - Наследует от `Employee` и добавляет атрибут `specialization` (специализация).
   - Метод `maintenance()` символизирует выполнение технического обслуживания.

4. **Создание класса `TechManager`**:
   - Наследует от `Manager` и `Technician`, комбинируя управленческие и технические навыки.
   - Добавляет методы для управления командой сотрудников.

5. **Демонстрация функциональности**:
   - Создаются объекты каждого класса, и демонстрируется их функциональность.

## Реализация

### Класс `Employee`
```python
class Employee:
    def __init__(self, name, id_number, sex, **kwargs):
        self.name = name
        self.id = id_number
        self.sex = sex
    def get_info(self):
        return f"{self.id} | {self.name} - {self.sex}"
```

### Класс `Manager`
```python
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
```

### Класс `Technician`
```python
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
```

### Класс `TechManager`
```python
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
```

### Пример использования
```python
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
```

## Заключение
В ходе выполнения лабораторной работы были освоены продвинутые концепции ООП в Python, такие как множественное наследование, инкапсуляция и полиморфизм. Учащиеся научились создавать сложные иерархии классов и комбинировать функциональность нескольких классов для решения практических задач.
