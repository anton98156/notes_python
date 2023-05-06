from datetime import datetime as dt

def id_logger(data):
    time = dt.now().strftime('\n%H:%M')
    with open('log.csv', 'a') as file:
        file.write('\nID: {};{};'
                   .format(data, time))

def name_logger(data):
    with open('log.csv', 'a') as file:
        file.write('\nЗаголовок заметки: {};'
                   .format(data))

def description_logger(data):
    with open('log.csv', 'a') as file:
        file.write('\nТело заметки: {};\n'
                   .format(data))