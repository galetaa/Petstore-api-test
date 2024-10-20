import pytest
from helpers.api_client import APIClient
from faker import Faker
import os

client = APIClient()
faker = Faker()


@pytest.fixture
def pet_data():
    return {
        "id": faker.random_int(min=1, max=100000),
        "name": faker.name(),
        "photoUrls": [faker.url()],
        "status": "available"
    }


def test_create_pet(pet_data):
    """
    Тест на создание нового питомца.
    """
    response = client.create_pet(pet_data)

    assert response.status_code == 200
    assert response.json()["name"] == pet_data["name"]


def test_get_pet_by_id(pet_data):
    """
    Тест на получение питомца по его ID.
    """
    client.create_pet(pet_data)
    response = client.get_pet(pet_data["id"])

    assert response.status_code == 200
    assert response.json()["id"] == pet_data["id"]


def test_delete_pet(pet_data):
    """
    Тест на удаление питомца.
    """
    client.create_pet(pet_data)
    response = client.delete_pet(pet_data["id"])

    assert response.status_code == 200

    response = client.get_pet(pet_data["id"])

    assert response.status_code == 404


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status(status):
    """
    Тест на поиск питомцев по статусу.
    """
    response = client.find_pets_by_status(status)

    assert response.status_code == 200

    pets = response.json()
    if pets:
        for pet in pets:

            assert pet["status"] == status


def test_upload_pet_image(pet_data):
    """
    Тест на загрузку изображения для питомца.
    """
    client.create_pet(pet_data)
    file_path = os.path.join(os.path.dirname(__file__), "test_image.jpg")
    with open(file_path, "wb") as f:
        f.write(os.urandom(1024))

    response = client.upload_pet_image(pet_data["id"], file_path, "Test image")

    assert response.status_code == 200
    assert "message" in response.json()

    os.remove(file_path)
