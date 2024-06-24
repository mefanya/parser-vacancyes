import pytest

from src.api import ApiHH
from src.vacancy import Vacancy
from src.job_list import JsonJobList


@pytest.fixture
def first_api():
    return ApiHH()


@pytest.fixture
def first_vacancy():
    return Vacancy(
        name="Python Developer",
        url="https://hh.ru/vacancy/test",
        salary=80000,
        description="Опыт работы не важен"
    )


@pytest.fixture
def second_vacancy():
    return Vacancy(
        name="Пайтон разработчик",
        url="https://hh.ru/vacancy/test2",
        salary=90000,
        description="Опыт работы от 1 года"
    )


@pytest.fixture
def first_job_list():
    return JsonJobList()
