import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import db
from app import app


class CafeRouteTests(unittest.TestCase):
    def setUp(self):
        self._original_config = {
            "DATABASE": app.config["DATABASE"],
            "TESTING": app.config["TESTING"],
        }
        self._temporary_directory = tempfile.TemporaryDirectory()
        database_path = Path(self._temporary_directory.name) / "test.sqlite"
        schema_path = Path(app.root_path) / "schema.sql"
        with sqlite3.connect(database_path) as connection:
            connection.executescript(schema_path.read_text(encoding="utf-8"))

        app.config.update(TESTING=True, DATABASE=str(database_path))
        self.client = app.test_client()

    def tearDown(self):
        app.config.update(self._original_config)
        self._temporary_directory.cleanup()

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
        self.assertIn(b"About this prototype", response.data)
        self.assertIn(b"Caf\xc3\xa9 Calle Ocho is a small EGN475 practice project.", response.data)
        self.assertIn(b'href="/"', response.data)

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

    def test_menu_uses_available_database_items_in_alphabetical_order(self):
        with sqlite3.connect(app.config["DATABASE"]) as connection:
            connection.execute(
                "INSERT INTO menu_items (name, category, price_cents, available) "
                "VALUES (?, ?, ?, ?)",
                ("Ajiaco Soup", "Soups", 1234, 1),
            )
            connection.execute(
                "INSERT INTO menu_items (name, category, price_cents, available) "
                "VALUES (?, ?, ?, ?)",
                ("Unavailable Special", "Seasonal", 999, 0),
            )

        response = self.client.get("/menu")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Ajiaco Soup", response.data)
        self.assertIn(b"$12.34", response.data)
        self.assertIn(b'href="/menu/10"', response.data)
        self.assertNotIn(b"Unavailable Special", response.data)
        names = [
            "Ajiaco Soup",
            "Citrus Sparkler",
            "Cortadito",
            "Cuban Sandwich",
            "Garden Toast",
            "Guava Pastry",
            "Mango Batido",
            "Medianoche Sandwich",
            "Morning Roast",
            "Zafra Coffee",
        ]
        with sqlite3.connect(app.config["DATABASE"]) as connection:
            connection.execute(
                "INSERT INTO menu_items (name, category, price_cents, available) "
                "VALUES (?, ?, ?, ?)",
                ("Zafra Coffee", "Hot Drinks", 400, 1),
            )
        response = self.client.get("/menu")
        positions = [response.data.index(name.encode("utf-8")) for name in names]
        self.assertEqual(positions, sorted(positions))

    def test_item_detail_page_displays_item(self):
        with sqlite3.connect(app.config["DATABASE"]) as connection:
            connection.execute(
                "UPDATE menu_items SET name = ?, price_cents = ? WHERE id = ?",
                ("Database Espresso", 425, 1),
            )

        response = self.client.get("/menu/1")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Database Espresso", response.data)
        self.assertIn(b"$4.25", response.data)
        self.assertIn(b'href="/menu"', response.data)

    def test_unknown_menu_item_returns_not_found(self):
        response = self.client.get("/menu/999")

        self.assertEqual(response.status_code, 404)

    def test_admin_menu_form_get_includes_fields_and_navigation_link(self):
        response = self.client.get("/admin/menu/new")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Add a Menu Item", response.data)
        self.assertIn(b'name="name"', response.data)
        self.assertIn(b'name="category"', response.data)
        self.assertIn(b'name="price"', response.data)
        self.assertIn(b'name="description"', response.data)
        self.assertIn(b'name="icon"', response.data)
        self.assertIn(b'href="/admin/menu/new"', response.data)

    def test_admin_menu_form_post_converts_price_and_persists_item(self):
        response = self.client.post(
            "/admin/menu/new",
            data={
                "name": "Pastelito de Coco",
                "category": "Pastries",
                "price": "0.29",
                "description": "Coconut pastry.",
                "icon": "🥥",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers["Location"], "/menu")
        with sqlite3.connect(app.config["DATABASE"]) as connection:
            item = connection.execute(
                "SELECT name, category, price_cents, description, icon, available "
                "FROM menu_items WHERE name = ?",
                ("Pastelito de Coco",),
            ).fetchone()

        self.assertEqual(
            item,
            ("Pastelito de Coco", "Pastries", 29, "Coconut pastry.", "🥥", 1),
        )
        response = self.client.get("/menu")
        self.assertIn(b"Pastelito de Coco", response.data)
        self.assertIn(b"$0.29", response.data)
        self.assertIn("Coconut pastry.".encode(), response.data)
        self.assertIn("🥥".encode(), response.data)

        response = self.client.get("/menu/10")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Pastelito de Coco", response.data)
        self.assertIn(b"$0.29", response.data)
        self.assertIn("Coconut pastry.".encode(), response.data)
        self.assertIn("🥥".encode(), response.data)

    def test_admin_menu_form_rejects_empty_or_whitespace_name(self):
        for name in ("", " \t "):
            with self.subTest(name=name):
                response = self.client.post(
                    "/admin/menu/new",
                    data={
                        "name": name,
                        "category": "Hot Drinks",
                        "price": "3.50",
                    },
                )
                self.assertEqual(response.status_code, 400)
                self.assertIn(b"Menu item name is required.", response.data)

        with sqlite3.connect(app.config["DATABASE"]) as connection:
            count = connection.execute(
                "SELECT COUNT(*) FROM menu_items"
            ).fetchone()[0]
        self.assertEqual(count, 9)

    def test_admin_menu_form_rejects_invalid_or_negative_prices(self):
        for price in ("-0.01", "1.234", "not-a-price", "NaN"):
            with self.subTest(price=price):
                response = self.client.post(
                    "/admin/menu/new",
                    data={
                        "name": "Invalid Price Item",
                        "category": "Specials",
                        "price": price,
                    },
                )
                self.assertEqual(response.status_code, 400)

        with sqlite3.connect(app.config["DATABASE"]) as connection:
            count = connection.execute(
                "SELECT COUNT(*) FROM menu_items"
            ).fetchone()[0]
        self.assertEqual(count, 9)

    def test_admin_menu_form_uses_parameterized_sql_for_item_name(self):
        injected_name = "Coffee'); DROP TABLE menu_items; --"
        response = self.client.post(
            "/admin/menu/new",
            data={
                "name": injected_name,
                "category": "Specials",
                "price": "1.00",
            },
        )

        self.assertEqual(response.status_code, 302)
        with sqlite3.connect(app.config["DATABASE"]) as connection:
            item = connection.execute(
                "SELECT name FROM menu_items WHERE name = ?",
                (injected_name,),
            ).fetchone()
            count = connection.execute(
                "SELECT COUNT(*) FROM menu_items"
            ).fetchone()[0]

        self.assertEqual(item, (injected_name,))
        self.assertEqual(count, 10)

    def test_uncommitted_insert_is_not_persisted_in_temporary_database(self):
        test_item_name = "Uncommitted Temporary Item"
        with app.app_context():
            connection = db.get_db()
            connection.execute(
                "INSERT INTO menu_items "
                "(name, category, price_cents, description, icon) "
                "VALUES (?, ?, ?, ?, ?)",
                (test_item_name, "Tests", 100, "", ""),
            )

        with sqlite3.connect(app.config["DATABASE"]) as connection:
            row = connection.execute(
                "SELECT id FROM menu_items WHERE name = ?",
                (test_item_name,),
            ).fetchone()
        self.assertIsNone(row)

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


class MenuDisplayMigrationTests(unittest.TestCase):
    def test_migration_refuses_to_create_a_missing_database(self):
        migration_path = (
            Path(__file__).parents[1]
            / "migrations"
            / "add_menu_item_display_fields.py"
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            database_path = Path(temporary_directory) / "missing.sqlite"
            result = subprocess.run(
                [sys.executable, str(migration_path), str(database_path)],
                capture_output=True,
                text=True,
            )
            self.assertFalse(database_path.exists())

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Database does not exist", result.stderr)

    def test_migration_preserves_existing_records_and_is_repeatable(self):
        migration_path = (
            Path(__file__).parents[1]
            / "migrations"
            / "add_menu_item_display_fields.py"
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            database_path = Path(temporary_directory) / "legacy.sqlite"
            with sqlite3.connect(database_path) as connection:
                connection.execute(
                    """
                    CREATE TABLE menu_items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        category TEXT NOT NULL,
                        price_cents INTEGER NOT NULL,
                        available INTEGER NOT NULL
                    )
                    """
                )
                connection.execute(
                    "INSERT INTO menu_items "
                    "(id, name, category, price_cents, available) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (1, "Café con Leche", "Hot Drinks", 350, 1),
                )
                connection.execute(
                    "INSERT INTO menu_items "
                    "(id, name, category, price_cents, available) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (2, "Custom Special", "Seasonal", 999, 1),
                )

            for _ in range(2):
                subprocess.run(
                    [sys.executable, str(migration_path), str(database_path)],
                    check=True,
                    capture_output=True,
                    text=True,
                )

            with sqlite3.connect(database_path) as connection:
                items = connection.execute(
                    "SELECT id, name, category, price_cents, available, "
                    "description, icon FROM menu_items ORDER BY id"
                ).fetchall()

        self.assertEqual(
            items,
            [
                (
                    1,
                    "Café con Leche",
                    "Hot Drinks",
                    350,
                    1,
                    "Cuban coffee with steamed milk.",
                    "☕",
                ),
                (2, "Custom Special", "Seasonal", 999, 1, "", ""),
            ],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
