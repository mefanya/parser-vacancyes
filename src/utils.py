from typing import Any
from src.vacancy import Vacancy


def user_interaction(vacancies_list: list[dict[str, Any]]):
    """
    Функция взаимодействия с пользователем

    :param vacancies_list: Список вакансий
    :return: Ничего не возвращает. Печатает отфильтрованные вакансии
    """
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_from = int(input("Введите зарплату от: "))

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_from)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


def filter_vacancies(vacancies_list: list[dict[str, Any]], filter_words: list) -> list[dict[str, Any]]:
    """
    Фильтрует список вакансий по ключевым словам из списка.

    :param vacancies_list: Список вакансий
    :param filter_words: Ключевые слова для фильтрации
    :return: возвращает отфильтрованный список вакансий
    """
    sorted_vacancy = []
    for vacancy in vacancies_list:
        for word in filter_words:
            if word in vacancy.get("name").split():
                sorted_vacancy.append(vacancy)

    return sorted_vacancy


def reformat_list_to_object(list_for_reformation: list[dict[str, Any]]) -> list[object]:
    """
    Превращает список вакансий в список объектов.

    :param list_for_reformation: Список вакансий
    :return: Список объектов вакансий
    """
    list_object = []
    for vacancy in list_for_reformation:
        list_object.append(Vacancy(name=vacancy.get("name"),
                                   url=vacancy.get("url"),
                                   salary=vacancy.get("salary"),
                                   description=vacancy.get("description")))

    return list_object


def get_vacancies_by_salary(vacancies: list[dict[str, Any]], salary_from: int) -> list[dict[str, Any]]:
    """
    Фильтрует вакансии по зарплате

    :param vacancies: Список вакансий
    :param salary_from: Минимальная зарплата
    :return: возвращает отфильтрованный список вакансий
    """
    vacancies_from = []
    for vacancy in vacancies:
        if vacancy.get("salary") == 0 or vacancy.get("salary").get("from") is None:
            continue
        if vacancy.get("salary").get("from") > salary_from:
            vacancies_from.append(vacancy)

    return vacancies_from


def sort_vacancies(vacancies: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Сортировка вакансий по зарплате от большего к меньшему

    :param vacancies: Список вакансий
    :return: Отсортированный список вакансий
    """
    sorted_vac = sorted(vacancies, key=lambda x: x["salary"]["from"], reverse=True)
    return sorted_vac


def get_top_vacancies(vacancies: list[dict[str, Any]], count_vac: int) -> list[dict[str, Any]]:
    """
    Срезает количество возвращаемых вакансий до заданного количества

    :param vacancies: Список вакансий
    :param count_vac: Количество вакансий
    :return: Отсортированный список вакансий
    """
    return vacancies[:count_vac]


def print_vacancies(vacancies: list[dict[str, Any]]):
    """
    Печатает вакансии с необходимыми параметрами

    :param vacancies: Список вакансий
    """
    for vacancy in vacancies:
        print(f"""
        Название вакансии: {vacancy.get("name")}
        Ссылка на вакансию: {vacancy.get("url")}
        Зарплата: {vacancy.get("salary").get("from")}
        Описание: {vacancy.get("description").get("requirement")}
        {vacancy.get("description").get("responsibility")}
        ________________________________________________________________
        """)
