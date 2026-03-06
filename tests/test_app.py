import unittest

from app import app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_route_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_expected_text(self):
        response = self.client.get("/")
        html = response.get_data(as_text=True)
        self.assertIn("Flask Starter is Running", html)
        self.assertIn("Server time:", html)

    def test_health_route_returns_ok_json(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_unknown_route_returns_404(self):
        response = self.client.get("/does-not-exist")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
