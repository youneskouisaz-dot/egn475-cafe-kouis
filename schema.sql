DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS menu_items;
DROP TABLE IF EXISTS users;

PRAGMA foreign_keys = ON;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'customer'
);

CREATE TABLE menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    icon TEXT NOT NULL DEFAULT '',
    price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
    available INTEGER NOT NULL DEFAULT 1 CHECK (available IN (0, 1))
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Pending',
    notes TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE RESTRICT
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    menu_item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
    FOREIGN KEY (menu_item_id) REFERENCES menu_items (id) ON DELETE RESTRICT
);

INSERT INTO users (id, username, password_hash, role) VALUES
    (1, 'sofia_m', 'sample-hash-not-for-authentication', 'customer'),
    (2, 'mateo_r', 'sample-hash-not-for-authentication', 'customer'),
    (3, 'lucia_p', 'sample-hash-not-for-authentication', 'customer');

INSERT INTO menu_items
    (id, name, category, description, icon, price_cents, available)
VALUES
    (1, 'Café con Leche', 'Hot Drinks', 'Cuban coffee with steamed milk.', '☕', 350, 1),
    (2, 'Cuban Sandwich', 'Sandwiches', 'Roasted pork, ham, Swiss cheese, and pickles.', '🥪', 850, 1),
    (3, 'Guava Pastry', 'Pastries', 'Flaky pastry filled with sweet guava.', '🥟', 300, 1),
    (4, 'Cortadito', 'Hot Drinks', 'Cuban espresso balanced with a touch of steamed milk.', '☕', 275, 1),
    (5, 'Medianoche Sandwich', 'Sandwiches', 'Roast pork, ham, Swiss, and pickles on soft sweet bread.', '🥪', 875, 1),
    (6, 'Mango Batido', 'Cold Drinks', 'A chilled mango milkshake blended until smooth.', '🥤', 450, 1),
    (7, 'Morning Roast', 'Hot Drinks', 'Medium-roast coffee with cocoa and caramel notes.', '☕', 325, 1),
    (8, 'Garden Toast', 'Breakfast', 'Herbed ricotta, seasonal greens, and lemon on sourdough.', '🍞', 850, 1),
    (9, 'Citrus Sparkler', 'Cold Drinks', 'Fresh orange, lemon, and sparkling water over ice.', '🍊', 400, 1);

INSERT INTO orders (id, user_id, customer_name, status, notes, created_at) VALUES
    (1043, 1, 'Sofia M.', 'Pending', '', '2026-11-22 13:28:00'),
    (1042, 2, 'Mateo R.', 'Preparing', '', '2026-11-22 13:24:00'),
    (1041, 3, 'Lucia P.', 'Ready', '', '2026-11-22 13:10:00');

INSERT INTO order_items (order_id, menu_item_id, quantity) VALUES
    (1043, 3, 2),
    (1043, 1, 1),
    (1042, 2, 1),
    (1042, 4, 2),
    (1041, 5, 1),
    (1041, 9, 1);
