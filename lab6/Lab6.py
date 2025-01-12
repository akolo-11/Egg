class UserAccount:
    def __init__(self, username = "", password = "", email = ""):
        self.username = username
        self.__password = password
        self.email = email

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return password == self.password


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

b = Car("susus", "amogus", "98")
print(b.get_info())
b.__class__ = Vehicle
print(b.get_info())
b.__class__ = Car
print(b.get_info())
a = UserAccount()
a.set_password("ewewe")
print(a.check_password("ewewe"))
print(a.check_password("sdsd"))