import os
import user_interface as ui

os.system("clear")

while True:
    command = str(input("Введите команду: "))
    if command == "add":
        ui.create_note()
    elif command == "exit": 
        break
    else:
        print("Такой команды не существует, попробуйте еще раз!")