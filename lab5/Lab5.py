class Book:
    title = ""
    author = ""
    year = 0
    def get_info(self):
        print("Book: " + self.title + ". Author: " + self.author + ". Year: " + str(self.year))
b1 = Book()
b1.title = "1"
b1.author = "2"
b1.year = 33
b1.get_info()

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius

c1 = Circle(2)
print(c1.get_radius())
c1.set_radius(3)
print(c1.get_radius())