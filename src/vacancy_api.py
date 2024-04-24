from abc import ABC, abstractmethod
import requests


class VacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, query):
        pass


class HeadHunterAPI(VacancyAPI):
    def get_vacancies(self, query):
        url = "https://api.hh.ru/vacancies"
        params = {"text": query, "area": "113"}  # area 113 соответствует России
        response = requests.get(url, params=params)
        return response.json()