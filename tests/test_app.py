import unittest

from app import app


class CafeRouteTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_home_page_returns_success(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Caf", response.data)
        self.assertIn(b"EGN475 Flask Prototype", response.data)

    def test_about_page_returns_success(self):
        response = self.client.get("/about")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About this prototype", response.data)
        self.assertIn(b"Flask request-to-response cycle", response.data)

    def test_home_navigation_links_to_about_page(self):
        response = self.client.get("/")

        self.assertIn(b'href="/about"', response.data)

    def test_unknown_route_returns_not_found(self):
        response = self.client.get("/not-a-real-page")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
