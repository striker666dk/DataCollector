import file_manager
import data_collector

def start():
    file_manager.create_files()
    data_collector.collect_data(file_manager.get_options())


start()