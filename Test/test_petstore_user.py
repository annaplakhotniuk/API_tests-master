from lib.assertion import Assertions
from lib.base_case import BaseCase
from lib.my_requests import MyRequests
import lib.logger
import json


class TestUserPetStore(BaseCase):
    def test_user_registration(self):
        """New create new user"""
        # Preparing the data input datas using
        registration_data = self.prepare_registration_data()
        registration_data_dict = json.dumps(registration_data)


        # Preparing datas for asserting
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        expected_username = registration_data["username"]
        expected_user_id = registration_data["id"]
        expected_keys = ["code", "type", "message"]
        expected_values = [200, "unknown", str(expected_user_id)]
        expected_dict = {
            "code": 200,
            "type": "unknown",
            "message": str(expected_user_id)
        }

        # Send 'POST' request on '/user' end point
        response_post = MyRequests.post("/user", data=registration_data_dict, headers=headers)

        # Check response datas
        Assertions.assert_status_code(response_post, 200)
        Assertions.assert_expected_dict(response_post, expected_dict)
        Assertions.assert_json_has_key(response_post, expected_keys)
        Assertions.assert_json_has_values(response_post, expected_values)

        """Get user by user name"""
        #Send 'GET' request on '/user/{username}' end point
        response = MyRequests.get(f"/user/{expected_username}")

        # Preparing the data for asserting
        expected_dict_get = registration_data_dict

        # Check response datas
        Assertions.assert_status_code(response, 200)
        Assertions.assert_value_by_name(response, expected_username)
        Assertions.assert_expected_dict(response, registration_data)


        """Put update user"""
        # Updated user datas
        registration_data_put = self.prepare_registration_data()
        registration_data_json = json.dumps(registration_data_put)


        # Send 'PUT' request on '/user/{username}'end point
        response_put = MyRequests.put(f"/user/{expected_username}", data=registration_data_json, headers=headers)

        # Preparing the data for asserting
        registration_data_put_dict = registration_data_put
        username_put = registration_data_put_dict["username"]
        expected_id = registration_data_put_dict["id"]
        expected_id_put = expected_id
        expected_dict_put = {
            "code": 200,
            "type": "unknown",
            "message": str(expected_id)
        }

        # Check response datas
        Assertions.assert_status_code(response, 200)
        Assertions.assert_expected_dict(response_put, expected_dict_put)

        """Get edited user"""
        # Send 'GET' request on '/user/{username}' end point
        response = MyRequests.get(f"/user/{username_put}")

        # Preparing the data for asserting
        expected_dict_get = registration_data_dict

        # Check response datas
        Assertions.assert_status_code(response, 200)
        Assertions.assert_value_by_name(response, expected_username)
        Assertions.assert_expected_dict(response, registration_data_put_dict)

        """Logs user into the system '/user/login'"""
        # Preparing  authorization datas
        login_pass = registration_data_put["password"]
        authorization_datas = {
            "username": str(expected_username),
            "password": str(login_pass)
        }
        # Send 'GET' request on '/user/login' end point
        response_login = MyRequests.get("/user/login", data=authorization_datas)

        # Preparing the data for asserting
        expected_dict_login = {
            "code": 200,
            "type": "unknown",
        }
        # Check response data
        Assertions.assert_status_code(response, 200)
        Assertions.assert_expected_dict(response_login, expected_dict_login)

        """Logs out current logged in user session on end point '/user/logout'"""
        # Send 'GET' request on '/user/logout' end point
        response_logout = MyRequests.get("/user/logout", headers=headers)

        # Preparing the data for asserting
        expected_dict_logout = {
            "code": 200,
            "type": "unknown",
            "message": "ok"
        }

        # Check response data
        Assertions.assert_status_code(response_logout, 200)
        Assertions.assert_expected_dict(response_logout, expected_dict_logout)

        """Delete user"""
        #Send 'GET' request on '/user/{username}'
        response_delete = MyRequests.get(f"/user/{expected_username}", headers=headers)

        # Check response data
        Assertions.assert_status_code(response_delete, 200)












