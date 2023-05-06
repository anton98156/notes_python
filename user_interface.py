import data_provider as provider
import logger as log

def id_view():
    string_id = provider.id_data()
    log.id_logger(string_id)

def name_view():
    string_name = provider.name_data()
    log.name_logger(string_name)

def description_view():
    string_description = provider.description_data()
    log.description_logger(string_description)