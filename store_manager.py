import requests
from bs4 import BeautifulSoup

class Store:

    number_of_stores = 0

    def __init__(self, name, url):
        self.name = name
        self.url = url
        Store.number_of_stores += 1

    def get_data_fakta(self):

        source_code = requests.get(self.url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        print(plain_text)

        for product in soup.findAll('div', {'class', 'dsp-entry'}):
            href = product.get('class')
            print (href)
            # header = BeautifulSoup(product).find('p', {'dsp-entry-heading'})
            # print header