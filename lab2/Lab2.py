from itertools import filterfalse


def greet(name):
    print("Hello, " + str(name))

def square(number):
    return number*number

def max_of_two(x, y):
    if x > y:
        return x
    return y

def describe_person(name, age = 30):
    print("The person's name is " + str(name) + '\n' + "The person's age is " + str(age))

def is_prime(number) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, round(number**.5) + 1, 2):
        if  number % i == 0:
            return False
    return True

greet("World")
print(square(7))
print(max_of_two(1, 5))
print(is_prime(1009))