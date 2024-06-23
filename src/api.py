from src.vacancy import Vacancy
from abc import ABC, abstractmethod
from typing import Any
import requests


class AbstractApi(ABC):
    @abstractmethod
    def _get_request(self, *args):
        pass


class ApiHH(AbstractApi):
    def __init__(self):
        self.URL = "https://api.hh.ru/vacancies"
        self.HEADERS = {'User-Agent': 'HH-User-Agent'}

    def _get_request(self, keyword: str, page: int):
        params = {
            "text": keyword,
            "page": page
        }
        return (requests.get(url=self.URL, params=params, headers=self.HEADERS)).json()

    @staticmethod
    def __processing_vacancies(vacancies: list[dict[str, Any]]) -> list:
        vacancies_processed = []
        for vacancy in vacancies:
            vacancies_processed.append(Vacancy(name=vacancy["name"],
                                               url=vacancy["alternate_url"],
                                               salary=vacancy["salary"],
                                               description=vacancy["snippet"]))

        return vacancies_processed

    def get_vacancies(self, keyword: str, page: int) -> list:
        return self.__processing_vacancies(self._get_request(keyword, page)["items"])
