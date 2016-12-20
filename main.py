from file_manager import *
from store_manager import Store

def collect_data():
    fakta = Store("fakta", "http://www.fakta.dk/tilbudsavis/")

    fakta.get_data_fakta()

collect_data()