import base64
import json
import os

import base64
import json
import os

import unittest

from application import create_app
from application.core.database import db
from tests.build_database import mock_db


class BaseTestClass(unittest.TestCase):
    def setUp(self):
        # mock authentification serivce, every jwt token is valid
        base_url = os.getenv("APIREST_AUTHENTIFICATION_SERVICE")
        url = f"{base_url}/v1/verify"
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Crea las tablas de la base de datos
        db.create_all()
        # mock database
        mock_db()
        self.client = self.app.test_client()
        # create fake autherization headers with jwt tokens
        self.fake_headers = {}
        self.fake_headers["admin"] = make_fake_headers(
            {
                "id": "250512d6-16e8-4161-8ac2-43501a7efe28",
                "username": "admin",
                "role": "admin",
            }
        )

        self.fake_headers["author"] = make_fake_headers(
            {
                "id": "67a3eb02-a099-4930-bb9e-d6a91cb46a9c",
                "username": "author",
                "role": "author",
            }
        )

        self.fake_headers["user"] = make_fake_headers(
            {
                "id": "749e10b4-9545-40ad-9f8a-8e41f08c817b",
                "username": "user",
                "role": "user",
            }
        )

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


def make_fake_headers(jwt_claims):
    token_template = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.%s.F3OLwaYV5mKgus82Soo2tE_ninlwlkg-5XtRt2njgu8"
    json_payload = json.dumps(
        {"user_claims": jwt_claims}, separators=(",", ":")
    ).encode("utf-8")
    encoded_token = (
        base64.urlsafe_b64encode(json_payload)
        .replace(b"=", b"")
        .decode("utf-8")
    )
    headers = {"Authorization": token_template % encoded_token}
    return headers
