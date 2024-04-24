from src.vacancy_api import HeadHunterAPI  # Импортируем класс для работы с API
from src.vacancy import Vacancy  # Импортируем класс вакансии
from src.saver import JSONSaver  # Импортируем класс для работы с файлами

def get_top_vacancies(vacancies_list, n):
    # Сортируем вакансии по минимальной зарплате и возвращаем топ-N
    return sorted(vacancies_list, key=lambda x: x.min_salary, reverse=True)[:n]

def find_vacancies_by_keyword(vacancies_list, keyword):
    # Фильтруем вакансии по наличию ключевого слова в описании
    return [vac for vac in vacancies_list if keyword.lower() in vac.description.lower()]

def user_interaction():
    hh_api = HeadHunterAPI()
    query = input("Введите поисковый запрос: ")
    vacancies_json = hh_api.get_vacancies(query)
    vacancies_list = Vacancy.cast_to_object_list(vacancies_json)

    # Получаем топ N вакансий по зарплате
    n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_vacancies = get_top_vacancies(vacancies_list, n)
    print("\nТоп вакансий по зарплате:")
    for vac in top_vacancies:
        print(f"{vac.title} - {vac.salary}")

    # Ищем вакансии с ключевым словом в описании
    keyword = input("\nВведите ключевое слово для поиска в описании: ")
    keyword_vacancies = find_vacancies_by_keyword(vacancies_list, keyword)
    print("\nВакансии с ключевым словом в описании:")
    for vac in keyword_vacancies:
        print(f"{vac.title} - {vac.description[:100]}...")

    # Запрос на сохранение данных
    save_data = input("\nХотите сохранить результаты запроса? (да/нет): ")
    if save_data.lower() == "да":
        saver = JSONSaver()
        for vacancy in vacancies_list:  # Сохраняем все вакансии полученные по запросу
            saver.add_vacancy(vacancy)
        print("Данные сохранены в файл vacancies.json в директории data.")

if __name__ == "__main__":
    user_interaction()