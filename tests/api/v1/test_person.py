import unittest
import json

from application.models.person import Person
from tests.base_test import BaseTestClass


class PersonTestCase(BaseTestClass):
    """Suite de tests del modelo Post"""

    def test_create_person(self):
        # add a user
        r = Person.query.filter_by(lname="Fairy").first()
        self.assertIsNotNone(r)

    # write an empty post
    def test_person_bad_request(self):
        data = {"fname": ""}
        response = self.client.post(
            "/api/v1/people", headers=self.get_api_headers(), json=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"'lname' is a required property", response.data)
        data = {"fname": "foo"}
        response = self.client.post(
            "/api/v1/people", headers=self.get_api_headers(), json=data
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"'lname' is a required property", response.data)

    def test_create_person(self):
        data = {"fname": "foo1", "lname": "bar1"}
        response = self.client.post(
            "/api/v1/people", headers=self.get_api_headers(), json=data
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"foo", response.data)
        self.assertIn(b"bar", response.data)

    def test_person_exist(self):
        data = {"fname": "Tooth", "lname": "Fairy"}
        response = self.client.post(
            "/api/v1/people", headers=self.get_api_headers(), json=data
        )
        self.assertEqual(response.status_code, 406)
        self.assertIn(
            b"Person with last name Fairy already exists", response.data
        )

    def test_read_all(self):
        response = self.client.get("/api/v1/people")
        self.assertEqual(response.status_code, 200)

    def test_read_one(self):
        data = {"fname": "Tooth", "lname": "Fairy"}
        response = self.client.get(f'/api/v1/people/{data["lname"]}')
        self.assertEqual(response.status_code, 200)

    def test_read_one_not_exist(self):
        data = {"fname": "Tooth", "lname": "Some"}
        response = self.client.get(f'/api/v1/people/{data["lname"]}')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Person with last name Some not found", response.data)

    def test_delete_person(self):
        data = {"fname": "Tooth", "lname": "Fairy"}
        response = self.client.delete(f'/api/v1/people/{data["lname"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Fairy successfully deleted", response.data)

    def test_delete_not_exist(self):
        data = {"fname": "Tooth", "lname": "Some"}
        response = self.client.delete(f'/api/v1/people/{data["lname"]}')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Person with last name Some not found", response.data)

    def test_update_person(self):
        data = {
            "lname": "Ruprecht",
            "fname": "Some",
        }
        response = self.client.put(
            f'/api/v1/people/{data["lname"]}',
            headers=self.get_api_headers(),
            data=json.dumps(data),
        )
        self.assertEqual(response.status_code, 201)

    def test_update_not_exist(self):
        data = {
            "lname": "Some",
            "fname": "Knecht",
        }
        response = self.client.put(
            f'/api/v1/people/{data["lname"]}',
            headers=self.get_api_headers(),
            data=json.dumps(data),
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Person with last name Some not found", response.data)

    def get_api_headers(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        return header


if __name__ == "__main__":
    unittest.main()
