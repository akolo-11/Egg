
# Лабораторная работа №6: Работа с классами ч.2

## Описание работы
В данной лабораторной работе рассматриваются более сложные аспекты объектно-ориентированного программирования (ООП) в Python, такие как инкапсуляция, наследование и полиморфизм. Учащиеся изучают, как защищать данные с помощью инкапсуляции, создавать иерархии классов с использованием наследования, а также переопределять методы для реализации полиморфизма. Работа включает два задания:

1. **Защита данных пользователя**: Учащиеся создают класс `UserAccount` с приватным атрибутом пароля и методами для его изменения и проверки.
2. **Полиморфизм и наследование**: Учащиеся создают базовый класс `Vehicle` и производный класс `Car`, переопределяя метод для вывода информации о транспортном средстве.

## Задание 1: Защита данных пользователя

### Реализация класса `UserAccount`
```python
class UserAccount:
    def __init__(self, username = "", password = "", email = ""):
        self.username = username
        self.__password = password
        self.email = email

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return password == self.password
```

## Задание 2: Полиморфизм и наследование

### Реализация классов `Vehicle` и `Car`
```python
class Vehicle:
    def __init__(self, make = None, model = None):
        self.make = make
        self.model = model

    def get_info(self):
        return self.make + " " + self.model


class Car(Vehicle):
    def __init__(self, make = None, model = None, fuel = None):
        super().__init__(make, model)
        self.fuel_type = fuel

    def get_info(self):
        return super().get_info() + " " + self.fuel_type
```

## Заключение
В ходе выполнения лабораторной работы были освоены более сложные концепции ООП в Python, такие как инкапсуляция, наследование и полиморфизм. Учащиеся научились защищать данные с помощью приватных атрибутов, создавать иерархии классов и переопределять методы для реализации полиморфного поведения.
