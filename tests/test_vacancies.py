def test_vacancy_first_init(first_vacancy):
    assert first_vacancy.name == "Python Developer"
    assert first_vacancy.url == "https://hh.ru/vacancy/test"
    assert first_vacancy.salary == 80000
    assert first_vacancy.description == "Опыт работы не важен"


def test_vacancy_second_init(second_vacancy):
    assert second_vacancy.name == "Пайтон разработчик"
    assert second_vacancy.url == "https://hh.ru/vacancy/test2"
    assert second_vacancy.salary == 90000
    assert second_vacancy.description == "Опыт работы от 1 года"


def test_compare_vacancies(first_vacancy, second_vacancy):
    assert first_vacancy > second_vacancy
