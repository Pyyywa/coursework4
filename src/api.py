import requests
import json
import os
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HH(AbstractAPI):
    def __init__(self, keyword, page=0):
        self.url = "https://api.hh.ru/vacansies/"
        self.params = {
            "text": keyword,
            "page": page
        }

    def get_vacanciest(self):
        return requests.get(self.url, params=self.params)
