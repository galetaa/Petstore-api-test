import pytest
from helpers.api_client import APIClient
from faker import Faker

client = APIClient()
faker = Faker()


def generate_user_data():
    """
    Генерация данных для одного пользователя.
    """
    return {
        "id": faker.random_int(min=1, max=1000),
        "username": faker.user_name(),
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "email": faker.email(),
        "password": faker.password(),
        "phone": faker.phone_number(),
        "userStatus": 1
    }


def test_create_user():
    """
    Тест на создание нового пользователя.
    """
    user_data = generate_user_data()
    response = client.create_user(user_data)

    assert response.status_code == 200


def test_create_users_with_list():
    """
    Тест на создание пользователей с помощью createWithList.
    """
    users = [generate_user_data() for _ in range(3)]
    response = client.create_users_with_list(users)

    assert response.status_code == 200


def test_create_users_with_array():
    """
    Тест на создание пользователей с помощью createWithArray.
    """
    users = [generate_user_data() for _ in range(2)]
    response = client.create_users_with_array(users)

    assert response.status_code == 200


def test_get_user_by_name():
    """
    Тест на получение пользователя по имени.
    """
    user_data = generate_user_data()
    client.create_user(user_data)
    response = client.get_user(user_data["username"])

    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]


def test_update_user():
    """
    Тест на обновление пользователя.
    """
    user_data = generate_user_data()
    client.create_user(user_data)

    updated_data = user_data.copy()
    updated_data["firstName"] = faker.first_name()
    response = client.update_user(user_data["username"], updated_data)

    assert response.status_code == 200


def test_delete_user():
    """
    Тест на удаление пользователя.
    """
    user_data = generate_user_data()
    client.create_user(user_data)
    response = client.delete_user(user_data["username"])

    assert response.status_code == 200

    response = client.get_user(user_data["username"])

    assert response.status_code == 404


def test_login_user():
    """
    Тест на авторизацию пользователя.
    """
    username = faker.user_name()
    password = faker.password()

    user_data = {
        "id": faker.random_int(min=1, max=1000),
        "username": username,
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "email": faker.email(),
        "password": password,
        "phone": faker.phone_number(),
        "userStatus": 1
    }
    client.create_user(user_data)

    response = client.login_user(username, password)

    assert response.status_code == 200


def test_logout_user():
    """
    Тест на выход пользователя из системы.
    """
    response = client.logout_user()

    assert response.status_code == 200
