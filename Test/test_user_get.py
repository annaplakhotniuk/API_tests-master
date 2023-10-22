import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertion import Assertions


@allure.epic("Authorization cases")
class TestUserGet(BaseCase):
    """"Create method with wrong credentials 'user_name'"""
    @allure.description("Sends 'GET' request with wrong credentials to endpoint /user/user")
    @allure.title("Test user details without authentication (negative)")
    def test_get_user_details_not_auth_negative(self):
        user_name = str(123456789123456789)
        expected_list_keys = ["code", "type", "message"]
        with allure.step("Send GET request with wrong credentials"):
            response = MyRequests.get(f"/user/{user_name}")

        with allure.step("Verify response status code and keys"):
            Assertions.assert_status_code(response, 404)
            Assertions.assert_has_keys(response, expected_list_keys)


    """Method for user authentication"""
    @allure.description("Sends request to check information about 'user'")
    @allure.title("Test user details with authentication")
    def test_get_user_details_auth_as_some_user(self):
        data = {
            "username": "SmokiMokiMo",
            "password": "9999999999999999999999999999999999999999999999999999999999999999999888877",
        }
        headers = {
            "accept": "application/json",
        }
        expected_list_keys = ["code", "type", "message"]
        with allure.step("Send authenticated GET request"):
            response = MyRequests.get("/user/login", data=data, headers=headers)

        with allure.step("Verify response status code and keys"):
            Assertions.assert_status_code(response, 200)
            Assertions.assert_has_keys(response, expected_list_keys)