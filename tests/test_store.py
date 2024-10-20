import pytest
from helpers.api_client import APIClient
from faker import Faker

client = APIClient()
faker = Faker()


def test_get_inventory():
    """
    Тест на получение инвентаря по статусам.
    """
    response = client.get_inventory()

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_place_order():
    """
    Тест на размещение заказа.
    """
    order_data = {
        "id": faker.random_int(min=1, max=1000),
        "petId": faker.random_int(min=1, max=1000),
        "quantity": 1,
        "shipDate": faker.date_time().isoformat(),
        "status": "placed",
        "complete": True
    }
    response = client.place_order(order_data)

    assert response.status_code == 200
    assert response.json()["status"] == order_data["status"]


def test_get_order_by_id():
    """
    Тест на получение заказа по его ID.
    """
    order_data = {
        "id": faker.random_int(min=1, max=1000),
        "petId": faker.random_int(min=1, max=1000),
        "quantity": 1,
        "shipDate": faker.date_time().isoformat(),
        "status": "placed",
        "complete": True
    }
    client.place_order(order_data)
    response = client.get_order(order_data["id"])

    assert response.status_code == 200
    assert response.json()["id"] == order_data["id"]


def test_delete_order():
    """
    Тест на удаление заказа.
    """
    order_data = {
        "id": faker.random_int(min=1, max=1000),
        "petId": faker.random_int(min=1, max=1000),
        "quantity": 1,
        "shipDate": faker.date_time().isoformat(),
        "status": "placed",
        "complete": True
    }
    client.place_order(order_data)
    response = client.delete_order(order_data["id"])

    assert response.status_code == 200

    response = client.get_order(order_data["id"])

    assert response.status_code == 404
