import os
import json

class JSONSaver:
    def __init__(self, filename='data/vacancies.json'):
        self.filename = filename
        # Создаём директорию, если она не существует
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def add_vacancy(self, vacancy):
        # Загружаем существующие вакансии из файла
        vacancies = self._load_vacancies()
        # Добавляем новую вакансию
        vacancies.append(vacancy.__dict__)
        # Сохраняем обновлённый список вакансий обратно в файл
        self._save_vacancies(vacancies)

    def _load_vacancies(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_vacancies(self, vacancies):
        with open(self.filename, 'w', encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)