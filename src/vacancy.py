class Vacancy:
    name: str
    url: str
    salary: int | None
    description: str | None
    vacancy_count = 0

    def __init__(self, name: str, url: str, salary: int | None, description: str | None):
        self.name = name
        self.url = url
        self.salary = self.validate(salary)
        self.description = description

    @staticmethod
    def validate(salary: int | None) -> int:
        return salary or 0
