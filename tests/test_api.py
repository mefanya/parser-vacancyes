def test_api_init(first_api):
    assert first_api.URL == "https://api.hh.ru/vacancies"
    assert first_api.HEADERS == {'User-Agent': 'HH-User-Agent'}


def test_api_get_request_one(first_api):
    result = first_api._get_request("Програмист пайтон", 1)

    if result:
        test = True
    else:
        test = False
    assert test is True


def test_api_get_vacancies_one(first_api):
    result = first_api.get_vacancies("Програмист пайтон", 1)

    if result:
        test = True
    else:
        test = False
    assert test is True
