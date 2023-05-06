import data_provider as provider
import logger as log


def name_view():
    string_name = provider.name_data()
    log.name_logger(string_name)

def description_view():
    string_description = provider.description_data()
    log.description_logger(string_description)

def create_note():
    name_view()
    description_view()
    print("Заметка успешно сохранена!")