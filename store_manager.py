class Store:

    number_of_stores = 0

    def __init__(self, name, url):
        self.name = name
        self.url = url
        Store.number_of_stores += 1

    def get_data_fakta(self):
        pass