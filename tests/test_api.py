import pytest
import requests_mock
from src.vacancy_api import HeadHunterAPI


# Фикстура pytest для создания экземпляра API
@pytest.fixture
def hh_api():
    return HeadHunterAPI()


def test_get_vacancies(hh_api):
    # URL для мокирования
    api_url = "https://api.hh.ru/vacancies"
    # Пример данных, которые должен вернуть мок
    mock_data = {"items": [{"id": "1", "name": "Python Developer"}]}

    with requests_mock.Mocker() as m:
        # Настройка мока
        m.get(api_url, json=mock_data)
        # Вызов тестируемого метода
        response = hh_api.get_vacancies("Python")
        # Проверки
        assert response["items"][0]["name"] == "Python Developer"
        # Проверяем, что был сделан запрос с корректными параметрами
        assert m.last_request.query == "text=Python&area=113"