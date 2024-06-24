from src.vacancy import Vacancy
from abc import ABC, abstractmethod
from typing import Any
import requests


class AbstractApi(ABC):
    """
    Абстрактный класс для работы с api разных ресурсов
    """
    @abstractmethod
    def _get_request(self, *args):
        pass


class ApiHH(AbstractApi):
    """
    Наследуемый класс для работы с api hh.ru
    """
    def __init__(self):
        self.URL = "https://api.hh.ru/vacancies"
        self.HEADERS = {'User-Agent': 'HH-User-Agent'}

    def _get_request(self, keyword: str, page: int):
        """
        Метод, который получает данные по запросу с hh.ru

        :param keyword: Запрос
        :param page: Страница (от 1 до 20)
        :return: Словарь. По ключу items можно получить словарь с вакансиями
        dict и необходимыми параметрами внутри
        """
        params = {
            "text": keyword,
            "page": page
        }
        return (requests.get(url=self.URL,
                             params=params,
                             headers=self.HEADERS)).json()

    @staticmethod
    def __processing_vacancies(vacancies: list[dict[str, Any]]) -> list:
        """
        Метод формирует вакансии (объекты) из полученных параметров

        :param vacancies: Список вакансий, где каждая вакансия это dict
        :return:
        """
        vacancies_processed = []
        for vacancy in vacancies:
            vacancies_processed.append(Vacancy(name=vacancy["name"],
                                               url=vacancy["alternate_url"],
                                               salary=vacancy["salary"],
                                               description=vacancy["snippet"]))

        return vacancies_processed

    def get_vacancies(self, keyword: str, page: int) -> list:
        """
        Публичный метод для получения уже обработанных вакансий.
        Получаем сразу список из объектов с нужными параметрами

        :param keyword: Запрос
        :param page: Страница (от 1 до 20)
        :return: Словарь. По ключу items можно получить словарь с вакансиями
        dict и необходимыми параметрами внутри
        """
        return self.__processing_vacancies(self._get_request(keyword,
                                                             page)["items"])
