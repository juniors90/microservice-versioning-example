import unittest
import json

from application.models.note import Note
from application.models.person import Person
from tests.base_test import BaseTestClass


class NoteTestCase(BaseTestClass):
    """Suite de tests del modelo Post"""

    def test_create_person(self):
        # add a user
        r = Note.query.filter_by(id=1).first()
        self.assertIsNotNone(r)

    # write an empty post
    def test_person_bad_request(self):
        data = {"fname": ""}
        response = self.client.post(
            "/api/v2/notes", headers=self.get_api_headers(), json=data
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Person not found for ID: None", response.data)

    def test_create_note(self):
        data = {"content": "string content", "person_id": 1}
        response = self.client.post(
            "/api/v2/notes", headers=self.get_api_headers(), json=data
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"string content", response.data)

    def test_read_one(self):
        data = {
            "content": "The other day a friend said, I have big teeth.",
            "id": 2,
            "person_id": 1,
            "timestamp": "2022-03-05T22:17:54",
        }
        response = self.client.get(f'/api/v2/notes/{data["id"]}')
        self.assertEqual(response.status_code, 200)

    def test_read_one_not_exist(self):
        data = {
            "content": "The other day a friend said, I have big teeth.",
            "id": 20,
            "person_id": 10,
            "timestamp": "2022-03-05T22:17:54",
        }
        response = self.client.get(f'/api/v2/notes/{data["id"]}')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Note with ID 20 not found", response.data)

    def test_update_person(self):
        data = {"content": "string"}
        response = self.client.put(
            f"/api/v2/notes/2",
            headers=self.get_api_headers(),
            data=json.dumps(data),
        )
        self.assertEqual(response.status_code, 201)

    def test_update_not_exist(self):
        data = {"content": "string"}
        response = self.client.put(
            f"/api/v2/notes/20",
            headers=self.get_api_headers(),
            data=json.dumps(data),
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Note with ID 20 not found", response.data)

    def test_delete_note(self):
        data = {
            "content": "Do you pay per gram?",
            "id": 3,
            "person_id": 1,
            "timestamp": "2022-03-05T22:18:10",
        }
        response = self.client.delete(f'/api/v2/notes/{data["id"]}')
        self.assertEqual(response.status_code, 204)

    def test_delete_not_exist(self):
        data = {
            "content": "The other day a friend said, I have big teeth.",
            "id": 20,
            "person_id": 10,
            "timestamp": "2022-03-05T22:17:54",
        }
        response = self.client.delete(f'/api/v2/notes/{data["id"]}')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Note with ID 20 not found", response.data)

    def get_api_headers(self):
        header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        return header


if __name__ == "__main__":
    unittest.main()
