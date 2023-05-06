import uuid

def id_data():
    data = uuid.uuid4()
    return data

def name_data():
    data = str(input("Введите заголовок заметки: "))
    return data

def description_data():
    data = str(input("Введите тело заметки: "))
    return data