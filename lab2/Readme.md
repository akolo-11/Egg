# Лабораторная работа №2: Функции в Python и базовые алгоритмы

## Цель работы
Освоить принципы определения и использования функций в языке программирования Python, понять механизмы передачи аргументов в функции, научиться применять функции для решения практических задач, а также изучить базовые алгоритмические конструкции.

## Задания

### Задание 1: Написание простых функций

1. **Функция `greet`**:
   - Принимает имя пользователя в качестве аргумента и выводит приветствие с этим именем.
   ```python
   def greet(name) -> None:
       print(f"Hello, {name}!")
   ```

2. **Функция `square`**:
   - Возвращает квадрат переданного ей числа.
   ```python
   def square(number) -> int | float | None:
       if isinstance(number, (int, float)):
           return number ** 2
       else:
           print("Вы передали не число!")
           return None
   ```

3. **Функция `max_of_two`**:
   - Принимает два числа в качестве аргументов и возвращает большее из них.
   ```python
   def max_of_two(x, y) -> int | float | None:
       if isinstance(x, (int, float)) and isinstance(y, (int, float)):
           return max(x, y)
       else:
           print("Функция принимает только числа")
           return None
   ```

### Задание 2: Работа с аргументами функций

1. **Функция `describe_person`**:
   - Принимает имя и возраст человека, и печатает эту информацию в читаемом виде. Возраст является опциональным аргументом со значением по умолчанию 30.
   ```python
   def describe_person(name, age=30) -> None:
       print(f"Имя: {name}")
       print(f"Возраст: {age}")
   ```

### Задание 3: Использование функций для решения алгоритмических задач

1. **Функция `is_prime`**:
   - Определяет, является ли число простым, и возвращает `True` или `False` соответственно.
   ```python
   def is_prime(number) -> bool:
       if not isinstance(number, int):
           return False
       if number <= 1:
           return False
       if number <= 3:
           return True

       divs = set()

       for i in range(1, int(number**0.5) + 1):
           if number % i == 0:
               divs.add(i)
               divs.add(number // i)

       return (sorted(divs)) == [1, number]
   ```

## Примеры использования функций

### Пример для задания 1
```python
def main():
    greet("Alex")
    print(square(5))
    print(max_of_two(1, 2))

if __name__ == "__main__":
    main()
```

### Пример для задания 2
```python
def main():
    describe_person("Alex", 20)

if __name__ == "__main__":
    main()
```

### Пример для задания 3
```python
def main():
    print(is_prime(7))

if __name__ == "__main__":
    main()
```

## Заключение
В ходе выполнения лабораторной работы были освоены принципы работы с функциями в Python, включая передачу аргументов, использование опциональных параметров и применение функций для решения алгоритмических задач.
