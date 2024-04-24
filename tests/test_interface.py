import json
from unittest import TestCase
from unittest.mock import patch, mock_open
from src.saver import JSONSaver
from main import get_top_vacancies, find_vacancies_by_keyword, user_interaction, Vacancy


class TestJSONSaver(TestCase):

    @patch("os.makedirs")
    def test_init_creates_directory(self, mock_makedirs):
        JSONSaver("some/directory/vacancies.json")
        mock_makedirs.assert_called_once_with("some/directory", exist_ok=True)

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.makedirs")
    def test_add_vacancy_saves_data(self, mock_makedirs, mock_file):
        saver = JSONSaver("vacancies.json")
        vacancy = {"title": "Software Engineer", "company": "Test Company"}  # Пример объекта вакансии
        saver.add_vacancy(vacancy)

        # Проверяем, был ли файл открыт для записи
        mock_file.assert_called_once_with("vacancies.json", "w")
        # Проверяем, что в файл были записаны корректные данные
        handle = mock_file()
        handle.write.assert_called_once()
        written_data = json.loads(handle.write.call_args[0][0])
        self.assertEqual(written_data, [vacancy])

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    @patch("os.makedirs")
    def test_load_vacancies_returns_empty_list_on_new_file(self, mock_makedirs, mock_file):
        saver = JSONSaver("vacancies.json")
        vacancies = saver._load_vacancies()
        self.assertEqual(vacancies, [])



def test_get_top_vacancies():
    vacancies_list = [
        Vacancy("Vacancy 1", "http://example.com", {"from": 2000}, ""),
        Vacancy("Vacancy 2", "http://example.com", {"from": 1000}, ""),
    ]
    top_vacancies = get_top_vacancies(vacancies_list, 1)
    assert len(top_vacancies) == 1
    assert top_vacancies[0].min_salary == 2000

def test_find_vacancies_by_keyword():
    vacancies_list = [
        Vacancy("Vacancy 1", "http://example.com", None, "We need Python developer"),
        Vacancy("Vacancy 2", "http://example.com", None, "Java position"),
    ]
    filtered_vacancies = find_vacancies_by_keyword(vacancies_list, "Python")
    assert len(filtered_vacancies) == 1
    assert "Python" in filtered_vacancies[0].description

@patch('builtins.input', side_effect=['Python developer', '2', 'Python', 'да'])
@patch('builtins.print')
@patch('your_script.JSONSaver.add_vacancy')
@patch('your_script.HeadHunterAPI.get_vacancies', return_value={"items": []})
def test_user_interaction(mock_get_vacancies, mock_add_vacancy, mock_print, mock_input):
    user_interaction()
    mock_get_vacancies.assert_called_once_with('Python developer')
    mock_add_vacancy.assert_called()  # Check if add_vacancy was called, indicating save attempt