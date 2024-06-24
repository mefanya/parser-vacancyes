from src.utils import user_interaction
from src.api import ApiHH
from src.job_list import JsonJobList


def main():
    count_pages = int(input("Сколько страниц хотите получить? "
                            "(От 1 до 100)\n"))

    search_query = input("Введите поисковый запрос: ")

    if count_pages <= 0:
        count_pages = 1
    elif count_pages > 100:
        count_pages = 100

    vacancies = []
    api = ApiHH()

    for i in range(1, count_pages):
        vacancies.extend(api.get_vacancies(search_query, i))

    list_vacancy = JsonJobList()
    list_vacancy.add_vacancy(vacancies)

    user_interaction(list_vacancy.get_data_from_file())


if __name__ == "__main__":
    main()
