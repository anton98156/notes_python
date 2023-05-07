import os
import user_interface as UI

def create_note():
    UI.id_view()
    UI.name_view()
    UI.description_view()
    print("Заметка успешно сохранена!")

def edit_notes():
    path = 'log.csv'
    os.remove(path)
    create_note()

def read_note_by_id(id):
    path = 'log.csv'
    data = open(path, 'r')
    list1 = [line.strip() for line in data.readlines()]
    for i, lines in enumerate(list1):
        if id in lines:
            print(list1[i])
            print(list1[i+1])
            print(list1[i+2])
            print(list1[i+3])
    data.close()

def read_note_by_date(date):
    path = 'log.csv'
    data = open(path, 'r')
    list1 = [line.strip() for line in data.readlines()]
    for i, lines in enumerate(list1):
        if date in lines:
            print(list1[i-1])
            print(list1[i])
            print(list1[i+1])
            print(list1[i+2])
    data.close()

def read_notes():
    path = 'log.csv'
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close() 

def delete_notes():
    path = 'log.csv'
    os.remove(path)