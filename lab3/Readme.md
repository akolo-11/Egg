# Лабораторная работа №3: Работа с файлами в Python

## Описание работы
В данной лабораторной работе рассматриваются основные принципы работы с файлами в языке программирования Python. Учащиеся изучают, как открывать, читать и записывать данные в файлы, а также обрабатывать исключения, которые могут возникнуть при работе с файловой системой. Работа включает три задания, каждое из которых направлено на освоение конкретных навыков:

1. **Открытие и чтение файла**: Учащиеся создают текстовый файл и пишут функцию для его чтения различными способами (чтение всего файла сразу или построчно).
2. **Запись в файл**: Учащиеся реализуют программу, которая записывает пользовательский текст в файл, а также добавляет текст в существующий файл без удаления предыдущего содержимого.
3. **Обработка исключений**: Учащиеся модифицируют программу для обработки исключений, таких как `FileNotFoundError`, чтобы программа корректно реагировала на попытки открыть несуществующий файл.

## Задание 1: Открытие и чтение файла

### Реализация функции для записи в файл
```python
def write_file(file_path: str):
    if not isinstance(file_path, str):
        print("Путь должен быть строкой")
        return
    try:
        with open(file_path, "w", encoding="UTF-8") as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line.\n")
            file.write("And this is the third line.\n")
    except FileNotFoundError:
        print("По заданному пути невозможно создать файл")
```

### Реализация функции для чтения файла с выбором метода
```python
def read_file_methods(file_path: str, method="all"):
    """
    Args:
        file_path (str): Path to txt file
        method (str, optional): _description_. Defaults to "all".
        all - read all file
        lines - read file by lines

    Returns:
        result (tuple): Selected method and file content
    """
    if not isinstance(file_path, str):
        print("Путь должен быть строкой")
        return "ERROR: Path must be a string"
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            if method == "all":
                # Чтение всего файла сразу
                content = file.read()

            elif method == "lines":
                # Чтение построчно
                content = ""
                for line in file:
                    content += line
            else:
                return "ERROR: This method is unsupported"
            return method, content
    except FileNotFoundError:
        print("По заданному пути невозможно прочитать файл")
```

### Пример использования
```python
if __name__ == "__main__":
    write_file("lab3/task1/example.txt")
    print(read_file_methods("lab3/task1/example.txt", "all"))
```

---

## Задание 2: Запись в файл

### Реализация функции для записи данных в файл
```python
def write_data_to_file(
    file_path: str,
    file_mode: str,
    user_input: str,
):
    if not isinstance(file_path, str):
        print("Путь должен быть строкой")
        return
    try:
        with open(file_path, file_mode, encoding="UTF-8") as file:
            file.write(user_input)
    except FileNotFoundError:
        print("По заданному пути невозможно создать файл")
    except ValueError:
        print("Указан неверный режим открытия файла", file_mode)
```

### Пример использования
```python
if __name__ == "__main__":
    write_data_to_file(
        file_path="lab3/task2/user_input.txt",
        file_mode="a",
        user_input="Hello, World!"
    )
```

---

## Заключение
В ходе выполнения лабораторной работы были освоены принципы работы с файлами в Python, включая чтение и запись данных, а также обработку исключений, таких как `FileNotFoundError`. Учащиеся научились создавать, читать и модифицировать файлы, а также обрабатывать ошибки, которые могут возникнуть при работе с файловой системой.
