def read_from_file():
    with open("grade.py", "r") as file:
        line = file.read()
    print(line)

read_from_file()