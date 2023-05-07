import os
import user_experience as UX

os.system("clear")

while True:
    command = str(input("\nВведите команду: "))
    command_split = command.split()
    if command_split[0] == "add":
        UX.create_note()
    elif command_split[0] == "edit": 
        UX.edit_notes()
    elif command_split[0] == "readByID": 
        UX.read_note_by_id(command_split[1])
    elif command_split[0] == "readByDate": 
        UX.read_note_by_date(command_split[1])
    elif command_split[0] == "read" and command_split[1] == "all": 
        UX.read_notes()
    elif command_split[0] == "delete": 
        UX.delete_notes()
    elif command_split[0] == "exit": 
        break
    else:
        print("Такой команды не существует, попробуйте еще раз!")