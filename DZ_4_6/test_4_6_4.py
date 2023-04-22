# Проверим правильность работы Яндекс.Диск REST API.
# Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test
# на верный ответ и возможные отрицательные тесты на ответы с ошибкой
# # Пример положительных тестов:
# # Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.

import requests

def test_positive_create_folder():
    headers = {"Authorization": "Bearer <your_token>"}
    params = {"path": "/test_folder"}
    response = requests.put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
    assert response.status_code == 201
    response = requests.get("https://cloud-api.yandex.net/v1/disk/resources?path=/")
    assert "test_folder" in response.json()['_embedded']['items']

def test_negative_create_folder_already_exists():
    headers = {"Authorization": "Bearer <your_token>"}
    params = {"path": "/test_folder"}
    response = requests.put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
    assert response.status_code == 409

def test_negative_create_folder_invalid_token():
    headers = {"Authorization": "Bearer <invalid_token>"}
    params = {"path": "/test_folder"}
    response = requests.put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
    assert response.status_code == 401