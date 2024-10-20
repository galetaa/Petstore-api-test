# Petstore API Tests

Этот проект содержит автоматизированные тесты для **Petstore API**, доступного по адресу [https://petstore.swagger.io](https://petstore.swagger.io).

## Что тестируется?

### **Питомцы (Pets)**

- **POST /pet**: Создание питомца
- **GET /pet/{petId}**: Получение питомца по ID
- **DELETE /pet/{petId}**: Удаление питомца по ID
- **GET /pet/findByStatus**: Поиск питомцев по статусу (`available`, `pending`, `sold`)
- **POST /pet/{petId}/uploadImage**: Загрузка изображения для питомца

### **Пользователи (Users)**

- **POST /user**: Создание нового пользователя
- **GET /user/{username}**: Получение пользователя по имени
- **PUT /user/{username}**: Обновление данных пользователя
- **DELETE /user/{username}**: Удаление пользователя
- **GET /user/login**: Логин пользователя
- **GET /user/logout**: Логаут пользователя
- **POST /user/createWithList**: Создание списка пользователей с помощью метода `createWithList`
- **POST /user/createWithArray**: Создание списка пользователей с помощью метода `createWithArray`

### **Магазин (Store)**

- **GET /store/inventory**: Получение инвентаря магазина по статусу
- **POST /store/order**: Размещение заказа для питомца
- **GET /store/order/{orderId}**: Получение информации о заказе по ID
- **DELETE /store/order/{orderId}**: Удаление заказа по ID

## Структура проекта

```
/tests
    ├── /test_pets.py          # Тесты для работы с питомцами
    ├── /test_users.py         # Тесты для работы с пользователями
    └── /test_store.py         # Тесты для работы с магазином
/helpers
    └── /api_client.py         # API клиент для взаимодействия с API
/config
    └── /config.py             # Конфигурация с базовым URL и API ключом (если требуется)
/requirements.txt              # Зависимости проекта
/pytest.ini                    # Конфигурация для Pytest (отчеты и другие настройки)
```

## Требования

Для запуска тестов необходимо:
- **Python 3.7+**
- Установленные библиотеки из файла `requirements.txt`

## Установка

1. Склонируйте репозиторий:

```bash
git clone https://github.com/galetaa/Petstore-api-test.git
```

2. Перейдите в каталог проекта:

```bash
cd petstore-api-tests
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Для запуска всех тестов используйте команду:

```bash
pytest
```

После выполнения тестов будет создан HTML-отчет.

### Запуск отдельных тестов

Вы можете запустить тесты для определенных компонентов, например, только для питомцев:

```bash
pytest tests/test_pets.py
```

