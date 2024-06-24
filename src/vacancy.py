class Vacancy:
    name: str
    url: str
    salary: int | None
    description: str | None

    def __init__(self, name: str, url: str, salary: int | None, description: str | None):
        self.name = name
        self.url = url
        self.salary = self.validate(salary)
        self.description = description

    def __gt__(self, other):
        if self.salary > other.salary:
            return self
        return other

    @staticmethod
    def validate(salary: int | None) -> int:
        return salary or 0
