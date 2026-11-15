import unittest

from app import app


class CafeRouteTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_home_page_returns_success(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Caf\xc3\xa9 Calle Ocho", response.data)
        self.assertIn(b"Today\xe2\x80\x99s caf\xc3\xa9 specials", response.data)
        self.assertIn(b"Morning Roast", response.data)
        self.assertIn(b'action="/cart/add/7"', response.data)

    def test_about_page_returns_success(self):
        response = self.client.get("/about")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Our caf\xc3\xa9", response.data)
        self.assertIn(b"neighborhood stop", response.data)
        self.assertIn(b'href="/menu"', response.data)

    def test_kitchen_board_uses_shared_layout_and_displays_sample_orders(self):
        response = self.client.get("/kitchen")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<a class="brand" href="/">Caf\xc3\xa9 Calle Ocho</a>', response.data)
        self.assertIn(b'href="/kitchen">Kitchen Board</a>', response.data)
        self.assertIn(b"Kitchen Board", response.data)
        self.assertIn(b"Order #1043", response.data)
        self.assertIn(b"Sofia M.", response.data)
        self.assertIn(b"2 \xc3\x97 Guava Pastry", response.data)
        self.assertIn(b"Order #1042", response.data)
        self.assertIn(b"Mateo R.", response.data)
        self.assertIn(b"Preparing", response.data)
        self.assertIn(b"Order #1041", response.data)
        self.assertIn(b"Lucia P.", response.data)
        self.assertIn(b"Ready for pickup", response.data)

    def test_order_history_uses_shared_layout_and_displays_all_sample_orders(self):
        response = self.client.get("/orders")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<a class="brand" href="/">Caf\xc3\xa9 Calle Ocho</a>', response.data)
        self.assertIn(b'href="/orders">Order History</a>', response.data)
        self.assertIn(b"Elena Garcia", response.data)
        self.assertIn(b"#1042", response.data)
        self.assertIn(b"Caf\xc3\xa9 con Leche", response.data)
        self.assertIn(b"$12.00", response.data)
        self.assertIn(b"Preparing", response.data)
        self.assertIn(b"Marcus Lee", response.data)
        self.assertIn(b"#1041", response.data)
        self.assertIn(b"$8.50", response.data)
        self.assertIn(b"Ready", response.data)
        self.assertIn(b"Isabella Cruz", response.data)
        self.assertIn(b"#1040", response.data)
        self.assertIn(b"$11.25", response.data)
        self.assertIn(b"Completed", response.data)

    def test_order_form_uses_shared_layout_and_displays_sample_menu(self):
        response = self.client.get("/order/new")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<a class="brand" href="/">Caf\xc3\xa9 Calle Ocho</a>', response.data)
        self.assertIn(b'href="/order/new">Order Form</a>', response.data)
        self.assertIn(b'<form class="order-form"', response.data)
        self.assertIn(b'name="customer_name"', response.data)
        self.assertIn(b'name="item_ids"', response.data)
        self.assertIn(b'name="quantity_1"', response.data)
        self.assertIn(b'name="notes"', response.data)
        self.assertIn(b"Caf\xc3\xa9 con Leche", response.data)
        self.assertIn(b"$3.50", response.data)
        self.assertIn(b"Order submission is not available yet", response.data)
        self.assertIn(b"disabled>Submit order (not available)", response.data)

    def test_order_form_previews_cart_quantities_and_total(self):
        self.client.post("/cart/add/1")
        self.client.post("/cart/add/1")
        self.client.post("/cart/add/7")

        response = self.client.get("/order/new")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'value="1" checked', response.data)
        self.assertIn(b'name="quantity_1" type="number" min="1" value="2"', response.data)
        self.assertIn(b"Morning Roast", response.data)
        self.assertIn(b"$10.25", response.data)

    def test_home_navigation_links_to_about_page(self):
        response = self.client.get("/")

        self.assertIn(b'href="/about"', response.data)
        self.assertIn(b'href="/menu"', response.data)

    def test_menu_page_lists_items_and_links_to_item_details(self):
        response = self.client.get("/menu")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Caf\xc3\xa9 Calle Ocho", response.data)
        self.assertIn(b"Caf\xc3\xa9 con Leche", response.data)
        self.assertIn(b"$3.50", response.data)
        self.assertIn(b'href="/menu/1"', response.data)
        self.assertGreaterEqual(response.data.count(b'class="menu-item"'), 6)

    def test_item_detail_page_displays_item(self):
        response = self.client.get("/menu/1")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Caf\xc3\xa9 con Leche", response.data)
        self.assertIn(b"$3.50", response.data)
        self.assertIn(b'href="/menu"', response.data)

    def test_unknown_menu_item_returns_not_found(self):
        response = self.client.get("/menu/999")

        self.assertEqual(response.status_code, 404)

    def test_cart_adds_items_from_today_and_full_menu_and_removes_items(self):
        response = self.client.post("/cart/add/7", data={"return_to": "home"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/#menu")

        response = self.client.post("/cart/add/1", data={"return_to": "menu"})
        self.assertEqual(response.status_code, 302)

        response = self.client.post("/cart/add/1", data={"return_to": "menu"})
        self.assertEqual(response.status_code, 302)

        response = self.client.get("/cart")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Morning Roast", response.data)
        self.assertIn(b"Caf\xc3\xa9 con Leche", response.data)
        self.assertIn(b"Quantity: 2", response.data)
        self.assertIn(b"$10.25", response.data)
        self.assertIn(b"Cart <span class=\"cart-count\">3</span>", response.data)

        response = self.client.post("/cart/remove/1")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/cart")
        self.assertIn(b"Morning Roast", response.data)
        self.assertNotIn(b"Caf\xc3\xa9 con Leche", response.data)
        self.assertIn(b"$3.25", response.data)

    def test_adding_unknown_item_returns_not_found(self):
        response = self.client.post("/cart/add/999")

        self.assertEqual(response.status_code, 404)

    def test_unknown_route_returns_not_found(self):
        response = self.client.get("/not-a-real-page")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)
