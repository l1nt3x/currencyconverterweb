# Импорт необходимых библиотек
import requests
from config import headers

# Задаем ключ API
headers = headers

# Функция получения последних курсов
def get_latest_rates(base='UAH', symbols='USD,EUR,RUB'):
    global headers
    # URL Запроса
    url = f"https://api.apilayer.com/fixer/latest?base={base}&symbols={symbols}"
    # Получаем ответ
    response = requests.request("GET", url, headers=headers)
    # Получаем код из ответа
    status_code = response.status_code
    # Получаем содержимое из ответа
    result = response.text
    # Меняем true на True, избегая NameError
    result = result.replace('true', 'True')
    # Делаем из словаря в строке обычный словарь
    result = eval(result)
    # Возвращаем результат
    return result


def get_currencies():
    global headers
    # URL Запроса
    url = f"https://api.apilayer.com/fixer/symbols"
    # Получаем ответ
    response = requests.request("GET", url, headers=headers)
    # Получаем код из ответа
    status_code = response.status_code
    # Получаем содержимое из ответа
    result = response.text
    # Меняем true на True, избегая NameError
    result = result.replace('true', 'True')
    # Делаем из словаря в строке обычный словарь
    result = eval(result)['symbols']
    # Возвращаем результат
    return result
