import unittest
import requests
from parameterized import parameterized

import app
from api.UserAPI import UserLgin
import json


def red_json():
    lins = []
    with open(app.workdir + "/data/login_data.json", "r", encoding="utf-8")as f:
        for value in json.load(f).values():
            username = value.get("username")
            password = value.get("password")
            verify_code = value.get("verify_code")
            status = value.get("status")
            msg = value.get("msg")
            ele = (username, password, verify_code, status, msg)
            lins.append(ele)
    return lins


class TestUser(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.userlgin = UserLgin()

    def tearDown(self):
        self.session.close()

    def test_get_verify_code(self):
        response = self.userlgin.get_verify_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))

    def test_login(self):
        response1 = self.userlgin.get_verify_code(self.session)
        response2 = self.userlgin.login(self.session, "13500000000", "123456", "8888")
        print(response2.json())

    @parameterized.expand(red_json())
    def test_loging(self, username, password, verify_code, status, mag):
        print("-" * 100)
        print(username, password, verify_code, status, mag)
        response1 = self.userlgin.get_verify_code(self.session)
        response2 = self.userlgin.login(self.session, username, password, verify_code)
        self.assertEqual(status, response2.json().get("status"))
        self.assertIn(mag, response2.json().get("msg"))
