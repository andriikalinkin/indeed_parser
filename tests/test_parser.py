import json

from indeed.parser import Parser


def test_parser_vacancy_class(list_with_html_vacancies):
    """Тест на парсинг html-блоков из списка объектом Parser."""
    vacancies = Parser()

    for html_vacancy in list_with_html_vacancies:
        vacancies.parse_n_save(html_vacancy)

    assert len(vacancies.get_vacancies) == len(list_with_html_vacancies), ('Количество обработанных вакансий не '
                                                                           'соответствует количеству html-вакансий')