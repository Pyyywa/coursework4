class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.description = description if description else ""
        self.min_salary = 0
        self.salary = "Зарплата не указана"

        if salary:
            if 'from' in salary and salary['from']:
                self.min_salary = salary['from']
                self.salary = f"от {salary['from']}"
            if 'to' in salary and salary['to']:
                self.salary += f" до {salary['to']}"
            if 'currency' in salary and salary['currency']:
                self.salary += f" {salary['currency']}"

    def __lt__(self, other):
        return self.min_salary < other.min_salary

    @staticmethod
    def cast_to_object_list(vacancies_json):
        vacancies = []
        for item in vacancies_json['items']:
            title = item['name']
            link = item['alternate_url']
            salary = item.get('salary', None)
            description = item.get('snippet', {}).get('requirement', '')
            vacancy = Vacancy(title, link, salary, description)
            vacancies.append(vacancy)
        return vacancies