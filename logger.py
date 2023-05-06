from datetime import datetime as dt

def name_logger(data):
    time = dt.now().strftime('\n%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}\nЗаголовок заметки: {};'
                   .format(time, data))

def description_logger(data):
    with open('log.csv', 'a') as file:
        file.write('\nТело заметки: {};'
                   .format(data))
