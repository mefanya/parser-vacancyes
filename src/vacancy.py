class Vacancy:
    """
    Класс для создания вакансии по переданным параметрам
    """
    name: str
    url: str
    salary: int | None
    description: str | None

    def __init__(self,
                 name: str,
                 url: str,
                 salary: int | None,
                 description: str | None):
        """
        Инициализация класса

        :param name: Название вакансии
        :param url: Ссылка на вакансию
        :param salary: Зарплата
        :param description: Описание
        """
        self.name = name
        self.url = url
        self.salary = self.validate(salary)
        self.description = description

    def __gt__(self, other):
        """
        Сравнение вакансий по зарплате.

        :return: Возвращает ту вакансию, зарплата в которой выше
        """
        if self.salary > other.salary:
            return self
        return other

    @staticmethod
    def validate(salary: int | None) -> int:
        """
        Статичный метод валидации зарплаты.
        """
        return salary or 0
