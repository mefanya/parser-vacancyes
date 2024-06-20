from abc import ABC, abstractmethod
import requests
import json


class AbstractApi(ABC):
    @abstractmethod
    def get_request(self, *args):
        pass


class ApiHH(AbstractApi):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {'User-Agent': 'HH-User-Agent'}

    def get_request(self, keyword, page):
        params = {
            "text": keyword,
            "page": page
        }
        return requests.get(url=self.url, params=params, headers=self.headers)
