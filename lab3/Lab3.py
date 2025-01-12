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

task_2("append")