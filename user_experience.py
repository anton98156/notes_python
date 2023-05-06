import user_interface as UI

def create_note():
    UI.id_view()
    UI.name_view()
    UI.description_view()
    print("Заметка успешно сохранена!")


def read_noteByID(id):
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

def edit_noteByID(id):
    path = 'log.csv'
    data = open(path, 'a+')
    # перезапись файла и удаление?
    # перечитать ТЗ
    data.close()

def read_noteByDate(date):
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