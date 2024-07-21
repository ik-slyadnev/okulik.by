# Meme API Testing Suite

- Этот проект представляет собой набор автоматизированных тестов для API управления мемами. 
- Тесты написаны с использованием Python и фреймворка pytest.

## Структура проекта

- meme-api-tests
  - endpoints
    - auth_endpoint.py
    - endpoints_handler.py
    - meme_endpoint.py
  - tests
    - test_auth.py 
    - test_create_meme.py 
    - test_get_meme.py 
    - test_update_meme.py

  - conftest.py
  - requirements.txt
  - README.md



## Описание тестов

- `test_auth.py`: Тесты для проверки функциональности авторизации.
- `test_create_meme.py`: Тесты для проверки создания новых мемов.
- `test_get_meme.py`: Тесты для проверки получения информации о мемах.
- `test_update_meme.py`: Тесты для проверки обновления существующих мемов.
- `test_delete_meme.py` : Тесты для удаления существующих мемов.

## Конфигурация

Настройки для тестов находятся в файле `conftest.py`.<br>
Здесь определены фикстуры и другие общие настройки для тестов.


