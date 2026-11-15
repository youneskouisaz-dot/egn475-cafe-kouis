import os
import secrets

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or secrets.token_hex(32)

SAMPLE_ITEMS = [
    {
        "id": 1,
        "name": "Café con Leche",
        "category": "Hot Drinks",
        "description": "Cuban coffee with steamed milk.",
        "price_cents": 350,
        "icon": "☕",
    },
    {
        "id": 2,
        "name": "Cuban Sandwich",
        "category": "Sandwiches",
        "description": "Roasted pork, ham, Swiss cheese, and pickles.",
        "price_cents": 850,
        "icon": "🥪",
    },
    {
        "id": 3,
        "name": "Guava Pastry",
        "category": "Pastries",
        "description": "Flaky pastry filled with sweet guava.",
        "price_cents": 300,
        "icon": "🥟",
    },
    {
        "id": 4,
        "name": "Cortadito",
        "category": "Hot Drinks",
        "description": "Cuban espresso balanced with a touch of steamed milk.",
        "price_cents": 275,
        "icon": "☕",
    },
    {
        "id": 5,
        "name": "Medianoche Sandwich",
        "category": "Sandwiches",
        "description": "Roast pork, ham, Swiss, and pickles on soft sweet bread.",
        "price_cents": 875,
        "icon": "🥪",
    },
    {
        "id": 6,
        "name": "Mango Batido",
        "category": "Cold Drinks",
        "description": "A chilled mango milkshake blended until smooth.",
        "price_cents": 450,
        "icon": "🥤",
    },
    {
        "id": 7,
        "name": "Morning Roast",
        "category": "Hot Drinks",
        "description": "Medium-roast coffee with cocoa and caramel notes.",
        "price_cents": 325,
        "icon": "☕",
    },
    {
        "id": 8,
        "name": "Garden Toast",
        "category": "Breakfast",
        "description": "Herbed ricotta, seasonal greens, and lemon on sourdough.",
        "price_cents": 850,
        "icon": "🍞",
    },
    {
        "id": 9,
        "name": "Citrus Sparkler",
        "category": "Cold Drinks",
        "description": "Fresh orange, lemon, and sparkling water over ice.",
        "price_cents": 400,
        "icon": "🍊",
    },
]

TODAY_MENU_IDS = {7, 8, 9}

SAMPLE_KITCHEN_ORDERS = [
    {
        "id": 1043,
        "customer_name": "Sofia M.",
        "items": [
            {"name": "Guava Pastry", "quantity": 2},
            {"name": "Café con Leche", "quantity": 1},
        ],
        "status": "Pending",
        "order_time": "1:28 PM",
    },
    {
        "id": 1042,
        "customer_name": "Mateo R.",
        "items": [
            {"name": "Cuban Sandwich", "quantity": 1},
            {"name": "Cortadito", "quantity": 2},
        ],
        "status": "Preparing",
        "order_time": "1:24 PM",
    },
    {
        "id": 1041,
        "customer_name": "Lucia P.",
        "items": [
            {"name": "Medianoche Sandwich", "quantity": 1},
            {"name": "Citrus Sparkler", "quantity": 1},
        ],
        "status": "Ready",
        "order_time": "1:10 PM",
    },
]

KITCHEN_STATUSES = ("Pending", "Preparing", "Ready")

SAMPLE_ORDER_HISTORY = [
    {
        "id": 1042,
        "customer_name": "Elena Garcia",
        "order_date": "Nov 14, 2026 · 1:24 PM",
        "items": [
            {"name": "Café con Leche", "quantity": 1, "price_cents": 350},
            {"name": "Cuban Sandwich", "quantity": 1, "price_cents": 850},
        ],
        "total_cents": 1200,
        "status": "Preparing",
    },
    {
        "id": 1041,
        "customer_name": "Marcus Lee",
        "order_date": "Nov 14, 2026 · 12:10 PM",
        "items": [
            {"name": "Guava Pastry", "quantity": 1, "price_cents": 300},
            {"name": "Cortadito", "quantity": 2, "price_cents": 275},
        ],
        "total_cents": 850,
        "status": "Ready",
    },
    {
        "id": 1040,
        "customer_name": "Isabella Cruz",
        "order_date": "Nov 13, 2026 · 4:30 PM",
        "items": [
            {"name": "Cortadito", "quantity": 1, "price_cents": 275},
            {"name": "Cuban Sandwich", "quantity": 1, "price_cents": 850},
        ],
        "total_cents": 1125,
        "status": "Completed",
    },
]


@app.get("/")
def home():
    """Render the cafe landing page."""
    today_items = [item for item in SAMPLE_ITEMS if item["id"] in TODAY_MENU_IDS]
    return render_template(
        "index.html",
        page_title="Home | Café Calle Ocho",
        today_items=today_items,
    )


@app.get("/about")
def about():
    """Render a page describing the prototype and its purpose."""
    return render_template("about.html", page_title="About | Café Calle Ocho")


@app.get("/kitchen")
def kitchen():
    """Render the display-only sample kitchen board."""
    orders_by_status = {
        status: [
            order
            for order in SAMPLE_KITCHEN_ORDERS
            if order["status"] == status
        ]
        for status in KITCHEN_STATUSES
    }
    return render_template(
        "kitchen.html",
        page_title="Kitchen Board | Café Calle Ocho",
        orders_by_status=orders_by_status,
    )


@app.get("/orders")
def orders():
    """Render the static sample order history."""
    return render_template(
        "orders.html",
        page_title="Order History | Café Calle Ocho",
        orders=SAMPLE_ORDER_HISTORY,
    )


@app.get("/order/new")
def order_new():
    """Render a display-only prototype order form."""
    cart_quantities = session.get("cart", {})
    items = [
        {
            **item,
            "cart_quantity": cart_quantities.get(str(item["id"]), 0),
            "line_total_cents": (
                item["price_cents"] * cart_quantities.get(str(item["id"]), 0)
            ),
        }
        for item in SAMPLE_ITEMS
    ]
    cart_items = [item for item in items if item["cart_quantity"] > 0]
    cart_total_cents = sum(item["line_total_cents"] for item in cart_items)

    return render_template(
        "order_new.html",
        page_title="Start an Order | Café Calle Ocho",
        items=items,
        cart_items=cart_items,
        cart_total_cents=cart_total_cents,
    )


@app.get("/menu")
def menu():
    """Render the sample café menu."""
    return render_template(
        "menu.html",
        page_title="Menu | Café Calle Ocho",
        items=SAMPLE_ITEMS,
    )


@app.get("/menu/<int:item_id>")
def item_detail(item_id):
    """Render a menu item's details or return not found."""
    item = next((sample for sample in SAMPLE_ITEMS if sample["id"] == item_id), None)
    if item is None:
        abort(404)

    return render_template(
        "item.html",
        page_title=f"{item['name']} | Café Calle Ocho",
        item=item,
    )


@app.get("/cart")
def cart():
    """Render the current session's shopping cart."""
    cart_quantities = session.get("cart", {})
    cart_items = []
    for item in SAMPLE_ITEMS:
        quantity = cart_quantities.get(str(item["id"]), 0)
        if quantity > 0:
            cart_items.append({**item, "quantity": quantity})

    total_cents = sum(item["price_cents"] * item["quantity"] for item in cart_items)
    return render_template(
        "cart.html",
        page_title="Your Cart | Café Calle Ocho",
        cart_items=cart_items,
        total_cents=total_cents,
    )


@app.post("/cart/add/<int:item_id>")
def cart_add(item_id):
    """Add one menu item to the current session's cart."""
    item = next((sample for sample in SAMPLE_ITEMS if sample["id"] == item_id), None)
    if item is None:
        abort(404)

    cart_quantities = session.get("cart", {})
    item_key = str(item_id)
    cart_quantities[item_key] = cart_quantities.get(item_key, 0) + 1
    session["cart"] = cart_quantities
    flash(f"{item['name']} added to your cart.")

    return_to = request.form.get("return_to")
    if return_to == "home":
        return redirect(url_for("home", _anchor="menu"))
    if return_to == "item_detail":
        return redirect(url_for("item_detail", item_id=item_id))
    return redirect(url_for("menu"))


@app.post("/cart/remove/<int:item_id>")
def cart_remove(item_id):
    """Remove a menu item from the current session's cart."""
    cart_quantities = session.get("cart", {})
    cart_quantities.pop(str(item_id), None)
    session["cart"] = cart_quantities
    return redirect(url_for("cart"))


@app.context_processor
def cart_count():
    """Expose the total number of items to the shared navigation."""
    return {"cart_count": sum(session.get("cart", {}).values())}


if __name__ == "__main__":
    app.run(debug=True)
