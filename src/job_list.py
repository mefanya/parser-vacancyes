import json
from abc import ABC, abstractmethod
from typing import Any


class AbstractList(ABC):
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
    def add_vacancy(self, vacancies: list):
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
        with open("data/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def del_vacancy(self):
        pass
