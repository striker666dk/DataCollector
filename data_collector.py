import requests
import time
import json
import os
import file_manager
from bs4 import BeautifulSoup

def collect_data(options):
    if not os.path.exists(options['DirName']):
        return

    while True:
        page = requests.get('http://borsen.dk/kurser/danske_aktier/c20_cap.html?tab=kurs')
        source_code = BeautifulSoup(page.text, 'html.parser')

        data = []
        for row in source_code.find_all('tr'):

            if row.find('td', {'class': 'stock-name first'}):
                aktie = row.find('a').getText().strip()
                performance_pct = row.find('td', {'class': 'PERFORMANCE_PCT'}).getText().strip()
                performance = row.find('td', {'class': 'PERFORMANCE'}).getText().strip()
                ydt = row.find('td', {'class': 'YDT'}).getText().strip()
                bid = row.find('td', {'class': 'BID'}).getText().strip()
                total_money = row.find('td', {'class': 'TOTAL_MONEY'}).getText().strip()

                item = json.dumps({
                    'aktie': aktie,
                    'performance_pct': performance_pct,
                    'performance': performance,
                    'ydt': ydt,
                    'bid': bid,
                    'total_money': total_money
                })

                data.append(item)

        file_manager.write_to_data(data)
        print('Data file updated...')

        time.sleep(options['Timer'])












