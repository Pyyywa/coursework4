import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_vacancy_initialization(self):
        salary_info = {"from": 1000, "to": 1500, "currency": "USD"}
        vacancy = Vacancy("Software Developer", "http://example.com", salary_info, "Good job")
        self.assertEqual(vacancy.title, "Software Developer")
        self.assertEqual(vacancy.link, "http://example.com")
        self.assertEqual(vacancy.description, "Good job")
        self.assertEqual(vacancy.min_salary, 1000)
        self.assertEqual(vacancy.salary, "от 1000 до 1500 USD")

    def test_vacancy_comparison(self):
        vacancy1 = Vacancy("Dev1", "http://example1.com", {"from": 500}, "")
        vacancy2 = Vacancy("Dev2", "http://example2.com", {"from": 1000}, "")
        self.assertTrue(vacancy1 < vacancy2)

    def test_cast_to_object_list(self):
        vacancies_json = {
            "items": [
                {"name": "Dev1", "alternate_url": "http://example1.com", "salary":
                    {"from": 500}, "snippet": {"requirement": ""}},
                {"name": "Dev2", "alternate_url": "http://example2.com", "salary":
                    {"from": 1000}, "snippet": {"requirement": ""}}
            ]
        }
        vacancies_list = Vacancy.cast_to_object_list(vacancies_json)
        self.assertEqual(len(vacancies_list), 2)
        self.assertIsInstance(vacancies_list[0], Vacancy)
        self.assertEqual(vacancies_list[0].title, "Dev1")
        self.assertEqual(vacancies_list[1].min_salary, 1000)


if __name__ == "__main__":
    unittest.main()