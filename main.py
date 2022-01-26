import csv
from abc import ABC
from typing import Optional, List, Type

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Chrome


class BaseCrawler(ABC):
    csv_headers: List[str]
    webdriver_class: Type[WebDriver]
    
    def __init__(self, csv_filename: str = None):
        csv_filename = self._get_csv_filename(csv_filename=csv_filename)
        self._driver = self.webdriver_class()
        self._csvfile = open(f'{csv_filename}', 'w', newline='', encoding='utf-8')
        self._writer = csv.DictWriter(self._csvfile, fieldnames=self.csv_headers)
        self._writer.writeheader()
    
    def _write_rows_list_to_csv(self, data: List[dict]):
        self._writer.writerows(data)
    
    def _write_row_dict_to_csv(self, data: dict):
        self._writer.writerow(data)

    def _get_csv_filename(self, csv_filename: Optional[str]) -> str:
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
            return f'{self.__class__.__name__.lower()}.csv'

    def __del__(self):
        self._driver.close()
        self._csvfile.close()


class SpendCrawler(BaseCrawler):
    csv_headers = ['Team', 'Forwards', 'Defense', 'Goalies', 'Injuries', 'Cap Hit']
    webdriver_class = Chrome