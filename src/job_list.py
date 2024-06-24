import json
from abc import ABC, abstractmethod
from typing import Any


class AbstractList(ABC):
    """
    Абстрактный класс для добавления и получения вакансий в необходимый файл
    """
    @abstractmethod
    def add_vacancy(self, vacancies: list):
        pass

    @abstractmethod
    def get_data_from_file(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class JsonJobList(AbstractList):
    """
    Наследуемый класс для добавления вакансий в файл json,
    а также получения из него вакансий обратно
    """
    def add_vacancy(self, vacancies: list):
        """
        Метод добавления вакансий в файл json

        :param vacancies: Список вакансий
        :return: Метод ничего не возвращает
        """
        with open("data/data.json", "r", encoding="utf-8") as file:
            list_ok: list[dict[str, Any]] = json.load(file)

        for vacancy in vacancies:
            list_ok.append({
                "name": vacancy.name,
                "url": vacancy.url,
                "salary": vacancy.salary,
                "description": vacancy.description
            })

        with open("data/data.json", "w+", encoding="utf-8") as file:
            json.dump(list_ok, file, ensure_ascii=False)

    def get_data_from_file(self) -> list[dict[str, Any]]:
        """
        Метод получения вакансий из файла

        :return: Возвращает список из словарей, где словарь - это вакансия
        """
        with open("data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def del_vacancy(self):
        """
        Метод будет удалять вакансии из файла.
        Будет дорабатываться после смены логики работы класса.
        :return:
        """
        pass
