import requests
from lib.base_case import BaseCase
from lib.assertion import Assertions
import json
from datetime import datetime

class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        date = self.prepare_registration_data()
        url = "https://petstore.swagger.io/v2/"
        response = requests.post(url, json=date)

        self.active_user_name = response.json()
        json_data = json.dumps(response.json())  # Convert data to JSON format
        parsed_data = json.loads(json_data)  # Parse the JSON data
        self.id_value = parsed_data["id"]  # Extract the value of "id"
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_id(response, "message")

    def test_create_user_with_existing_email(self):
        """Credentials"""
        email = 'email@gmail.com'
        """Sending data (with invalid request data 'ID')"""
        date = {
            "id": 12345678912345678911,
            "username": "user_name_test",
            "firstName": "first_name_test",
            "lastName": "last_name_string",
            "email": email,
            "password": "password_123",
            "phone": "0966050097",
            "userStatus": 0
        }
        """Request headers"""
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(self.url, json=date, headers=headers)

        Assertions.assert_status_code(response, 500)
        Assertions.assert_json_has_key(response, "message")

