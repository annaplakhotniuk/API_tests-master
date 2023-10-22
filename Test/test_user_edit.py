import json
import allure
from lib.base_case import BaseCase
from lib.assertion import Assertions
from lib.my_requests import MyRequests
import pytest


@allure.epic("Performs main API points Register/Login/Login/Edit/GetUser. ")
class TestUserEdit(BaseCase):
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    expected_dict = {}

    @allure.description("This test create new user")
    def test_create_new_user(self, new_user_credentials):
        registration_data_str, generate_new_user_cred, expected_dict, username, login_data = new_user_credentials
        with allure.step("Send POST request with automatically generated credentials"):
            response_user = MyRequests.post("/user", data=registration_data_str, headers=self.headers)
        with allure.step("Verify response status code and data"):
            Assertions.assert_status_code(response_user, 200)
            Assertions.assert_expected_dict(response_user, expected_dict)

    @allure.description("This test successfully perform login new user")
    def test_user_login(self, new_user_credentials):
        login_data = new_user_credentials[-1]
        with allure.step("Send GET request with login and password credentials"):
            response_login = MyRequests.get("/user/login", data=login_data)
        with allure.step("Verify response status code"):
            Assertions.assert_status_code(response_login, 200)

    @allure.description("This test successfully perform logout new user")
    def test_user_logout(self):
        with allure.step("Send GET request to perform logout"):
            response_logout = MyRequests.get(f"/user/logout", headers=self.headers)
        with allure.step("Verify response status code"):
            Assertions.assert_status_code(response_logout, 200)

    @allure.description("This test successfully add some information for new user")
    def test_user_edit(self, new_user_credentials):
        registration_data = self.prepare_registration_data()
        self.expected_dict = registration_data
        data_put_str = json.dumps(registration_data)
        with allure.step("Send PUT request, performs data modification"):
            response_edit = MyRequests.put(f"/user/{new_user_credentials[3]}", data=data_put_str, headers=self.headers)
        with allure.step("Verify response status code"):
            Assertions.assert_status_code(response_edit, 200)

    @allure.description("This test successfully checks changed information about new user")
    def test_user_get_info(self, new_user_credentials):

        with allure.step("Send PUT request, performs data modification"):
            response_get = MyRequests.get(f"/user/{new_user_credentials[3]}", headers=self.headers)
        with allure.step("Verify response status code and keys"):
            Assertions.assert_status_code(response_get, 200)
            Assertions.assert_expected_dict(response_get, self.expected_dict)


    # @allure.description("This test delete user")
    # def test_delete_user(self, new_user_credentials):
    #     with allure.step("Send GET request, to deleting a user"):
    #         response_delete = MyRequests.delete(f"/user/{new_user_credentials[3]}", headers=self.headers)
    #     with allure.step("Verify response status code"):
    #         Assertions.assert_status_code(response_delete, 200)
