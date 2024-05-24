import unittest

from fastapi.testclient import TestClient

from src.main import app


class TestV1RouteHealth(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_health(self):
        response = self.client.get("/api/v1/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
