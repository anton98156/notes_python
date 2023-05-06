import user_interface as UI

def create_note():
    UI.id_view()
    UI.name_view()
    UI.description_view()
    print("Заметка успешно сохранена!")

def read_note():
    path = 'log.csv'
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close() 