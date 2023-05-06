import os
import user_experience as UX

os.system("clear")

while True:
    command = str(input("\nВведите команду: "))
    if command == "add":
        UX.create_note()
    elif command == "read all": 
        UX.read_note()
    elif command == "exit": 
        break
    else:
        print("Такой команды не существует, попробуйте еще раз!")