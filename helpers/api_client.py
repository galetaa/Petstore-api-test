import requests
import logging
from config.config import BASE_URL

logging.basicConfig(level=logging.INFO)


class APIClient:
    # Питомцы (Pets)
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.headers = {"Authorization": "Bearer {}"}

    def create_pet(self, pet_data):
        logging.info(f"Creating pet with data: {pet_data}")
        response = requests.post(f"{self.base_url}/pet", json=pet_data, headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def get_pet(self, pet_id):
        logging.info(f"Getting pet with ID: {pet_id}")
        response = requests.get(f"{self.base_url}/pet/{pet_id}", headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def delete_pet(self, pet_id):
        logging.info(f"Deleting pet with ID: {pet_id}")
        response = requests.delete(f"{self.base_url}/pet/{pet_id}", headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def find_pets_by_status(self, status):
        logging.info(f"Finding pets by status: {status}")
        params = {"status": status}
        response = requests.get(f"{self.base_url}/pet/findByStatus", params=params, headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def upload_pet_image(self, pet_id, file_path, additional_metadata=""):
        logging.info(f"Uploading image for pet ID: {pet_id}")
        files = {"file": open(file_path, "rb")}
        data = {"additionalMetadata": additional_metadata}
        response = requests.post(f"{self.base_url}/pet/{pet_id}/uploadImage", files=files, data=data,
                                 headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    # Магазин (Store)
    def get_inventory(self):
        logging.info("Getting inventory")
        response = requests.get(f"{self.base_url}/store/inventory", headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def place_order(self, order_data):
        logging.info(f"Placing order with data: {order_data}")
        response = requests.post(f"{self.base_url}/store/order", json=order_data, headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def get_order(self, order_id):
        logging.info(f"Getting order with ID: {order_id}")
        response = requests.get(f"{self.base_url}/store/order/{order_id}", headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def delete_order(self, order_id):
        logging.info(f"Deleting order with ID: {order_id}")
        response = requests.delete(f"{self.base_url}/store/order/{order_id}", headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    # Пользователи (Users)
    def create_user(self, user_data):
        logging.info(f"Creating user with data: {user_data}")
        response = requests.post(f"{self.base_url}/user", json=user_data, headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def get_user(self, username):
        logging.info(f"Getting user with username: {username}")
        response = requests.get(f"{self.base_url}/user/{username}", headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def update_user(self, username, user_data):
        logging.info(f"Updating user {username} with data: {user_data}")
        response = requests.put(f"{self.base_url}/user/{username}", json=user_data, headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def delete_user(self, username):
        logging.info(f"Deleting user with username: {username}")
        response = requests.delete(f"{self.base_url}/user/{username}", headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def login_user(self, username, password):
        logging.info(f"Logging in user with username: {username}")
        params = {"username": username, "password": password}
        response = requests.get(f"{self.base_url}/user/login", params=params)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def logout_user(self):
        logging.info(f"Logging out current user")
        response = requests.get(f"{self.base_url}/user/logout", headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def create_users_with_list(self, users):
        logging.info(f"Creating users with list: {users}")
        response = requests.post(f"{self.base_url}/user/createWithList", json=users, headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response

    def create_users_with_array(self, users):
        logging.info(f"Creating users with array: {users}")
        response = requests.post(f"{self.base_url}/user/createWithArray", json=users, headers=self.headers)
        logging.info(f"Response: {response.status_code}, {response.text}")
        return response
