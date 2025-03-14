# Лабораторная работа №3: Работа с файлами в Python

## Описание работы
В данной лабораторной работе рассматриваются основные принципы работы с файлами в языке программирования Python. Учащиеся изучают, как открывать, читать и записывать данные в файлы, а также обрабатывать исключения, которые могут возникнуть при работе с файловой системой. Работа включает три задания, каждое из которых направлено на освоение конкретных навыков:

1. **Открытие и чтение файла**: Учащиеся создают текстовый файл и пишут функцию для его чтения различными способами (чтение всего файла сразу или построчно).
2. **Запись в файл**: Учащиеся реализуют программу, которая записывает пользовательский текст в файл, а также добавляет текст в существующий файл без удаления предыдущего содержимого.
3. **Обработка исключений**: Учащиеся модифицируют программу для обработки исключений, таких как `FileNotFoundError`, чтобы программа корректно реагировала на попытки открыть несуществующий файл.

## Задание 1 & 3: Открытие и чтение файла с обработкой исключения
```python
def task_1(mode = "whole"):
    try:
        if mode == "whole":
            with open("example.txt", "r") as file:
                print(file.read())
                file.close()
        elif mode == "linear":
            with open("example.txt", 'r') as file:
                for line in file:
                    print(line, end="")
                file.close()
    except FileNotFoundError:
        print("file does not exist")
```

---

## Задание 2: Запись в файл
```python
def task_2(mode = "overwrite"):
    file_name = "user_input.txt"
    text = ""
    string = input("Enter text line by line [exit() to finish]:\n")
    while string != "exit()":
        text += string
        text += "\n"
        string = input()
    if text != "":
        text = text[:-1]
    if mode == "overwrite":
        file = open(file_name, "w")
    elif mode == "append":
        file = open(file_name, "a")
    else:
        return
    file.write(text)
    file.close()
```

---

## Заключение
В ходе выполнения лабораторной работы были освоены принципы работы с файлами в Python, включая чтение и запись данных, а также обработку исключений, таких как `FileNotFoundError`. Учащиеся научились создавать, читать и модифицировать файлы, а также обрабатывать ошибки, которые могут возникнуть при работе с файловой системой.
