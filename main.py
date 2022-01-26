import csv
from typing import Optional

from selenium import webdriver


class SpendCrawler:
    def __init__(self, csv_filename: str = None) -> None:
        csv_filename = self.get_csv_filename(csv_filename=csv_filename)
        self.driver: webdriver.Chrome = webdriver.Chrome()
        field_names = ['Team', 'Forwards', 'Defense', 'Goalies', 'Injuries', 'Cap Hit']
        self.csvfile = open(f'{csv_filename}', 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.csvfile, fieldnames=field_names)
        self.writer.writeheader()

    def get_csv_filename(self, csv_filename: Optional[str]) -> str:
        '''
        If a csv_filename is provided, return it. Otherwise, return 'spend.csv'.
        
        :param csv_filename: The name of the CSV file to write to. If not specified, the default is
        'spend.csv'
        :type csv_filename: Optional[str]
        :return: The csv_filename is being returned.
        '''
        if csv_filename:
            if csv_filename.endswith('.csv'):
                return csv_filename
            else:
                return f'{csv_filename}.csv'
        else:
            return 'spend.csv'
    
    def __del__(self):
        self.driver.close()
        self.csvfile.close()