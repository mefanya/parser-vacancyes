from src.utils import (filter_vacancies, get_vacancies_by_salary,
                       sort_vacancies, get_top_vacancies)


def test_filter_vacancies(list_before, list_for_test_filter_vacancies):
    result = filter_vacancies(list_before, ["разработчик",
                                            "специалист",
                                            "Специалист"])
    assert result == list_for_test_filter_vacancies


def test_get_vacancies_by_salary(list_before,
                                 list_for_get_vacancies_by_salary_after):
    result = get_vacancies_by_salary(list_before, 50000)
    assert result == list_for_get_vacancies_by_salary_after


def test_sort_vacancies(list_for_get_vacancies_by_salary_after,
                        list_for_sort_vacancies_after):
    result = sort_vacancies(list_for_get_vacancies_by_salary_after)
    assert result == list_for_sort_vacancies_after


def test_get_top_vacancies(list_for_sort_vacancies_after,
                           list_for_get_top_vacancies_after):
    result = get_top_vacancies(list_for_sort_vacancies_after, 2)

    assert result == list_for_get_top_vacancies_after
