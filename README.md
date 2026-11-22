<div align="center">

# Café Calle Ocho

### A neighborhood café, a clearer path from order to pickup.

**An EGN475 educational Flask prototype concept for a Cuban café in Little Havana, Miami.**

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![GitHub repository](https://img.shields.io/badge/GitHub-public%20repository-181717?logo=github&logoColor=white)](https://github.com/youneskouisaz-dot/egn475-cafe-kouis)
[![Project status](https://img.shields.io/badge/Project%20status-prototype%20planning-9A5B32)](#academic-milestones)

</div>

> **Scope note:** This application began as the Assignment 1.1 Café Kouis starter and now includes the Café Calle Ocho prototype: a SQLite-backed menu, session cart, display-only order and kitchen pages, and an unauthenticated staff menu-item creation form. Order submission, status updates, and authentication are not implemented.

## Contents

- [Project overview](#project-overview)
- [Why Option A](#why-option-a)
- [Problem statement](#problem-statement)
- [Target personas](#target-personas)
- [Prototype scope](#prototype-scope)
- [User journeys](#user-journeys)
- [Current application](#current-application)
- [Getting started on Windows](#getting-started-on-windows)
- [Project structure](#project-structure)
- [Academic milestones](#academic-milestones)

## Project overview

Café Calle Ocho is a proposed small web prototype for a Cuban café in Little Havana, Miami. Its intended workflow connects a customer-facing menu and ordering experience with a simple kitchen order board. Customers would be able to follow an order from placement through pickup, while staff would see clear tickets and status changes.

This repository is an **EGN475 educational project**, not a production ordering service. The current prototype includes a SQLite-backed menu, session cart, sample kitchen and order-history pages, and an unauthenticated staff menu-item form. Order submission and kitchen status updates remain future development.

## Why Option A

I chose **Option A — Café Calle Ocho** because a café ordering workflow is practical, familiar, and well suited to a small web prototype. It gives the project a concrete customer journey and a straightforward staff workflow to explore without requiring a large system.

## Problem statement

> Café Calle Ocho currently handles customer orders through face-to-face conversations and handwritten tickets. This can cause longer wait times, unclear order status, and mistakes for customers and kitchen staff during busy periods. Our prototype will allow customers to view the menu and place orders online while staff track orders from received to picked up, helping make service more organized and efficient.

**Project assumption, not verified business research:** The current-workflow description above is an assumption for defining the prototype problem. It has not been confirmed with Café Calle Ocho or another actual business.

## Target personas

### Marta Alvarez — Customer

**Age:** 34 · **Context:** Stops at the café before work.

- **Goal:** Place an accurate order quickly and keep the wait short.
- **Frustration:** Lines and uncertainty about when an order will be ready.
- **Technology comfort:** Comfortable with smartphones and basic apps.
- **Quote:** “I just want to order my coffee quickly and know when it's ready.”

### Luis Rodriguez — Kitchen employee

**Age:** 29 · **Context:** Handles multiple orders during rush periods.

- **Goal:** See clear tickets and current order statuses.
- **Frustration:** Difficult-to-read handwritten notes and repeated questions about status.
- **Technology comfort:** Comfortable with simple touchscreen interfaces.
- **Quote:** “Show me what to prepare next and which orders are ready.”

## Prototype scope

These are the **must-have features for the planned prototype**. Some are implemented in display-only or prototype form; current behavior is listed below.

1. Browse the café menu.
2. Select menu items.
3. Place an order.
4. Show an order confirmation with an ID.
5. Display a kitchen order board.
6. Update order status through **Received → Preparing → Ready → Picked Up**.
7. Provide order history and basic menu administration. A menu-item creation form is implemented; authentication and editing or deleting menu items remain future work.

### Out of scope

- Online payment processing
- SMS or email notifications
- Native mobile applications
- Loyalty and rewards systems
- Third-party delivery integrations

## User journeys

**Customer:** Opens the menu → selects items → reviews and places the order → receives a confirmation ID → checks progress → picks up the order when its status is **Ready**.

**Kitchen staff:** Opens the order board → reviews new **Received** tickets → marks a ticket **Preparing** → marks it **Ready** when complete → marks it **Picked Up** after handoff. The planned board is intended to make the next work and each order's status easy to see.

## Current application

`app.py` creates the Flask application and defines:

| Route | Current behavior |
| --- | --- |
| `/` | Renders the existing home-page template. |
| `/about` | Renders the existing prototype information page. |
| `/menu`, `/menu/<int:item_id>` | Read available menu items and item details from SQLite. |
| `/admin/menu/new` | Displays a staff menu-item form and saves submitted items to SQLite. Authentication is not enabled. |
| `/cart`, `/order/new` | Maintain a session cart and render a display-only order preview. |
| `/kitchen`, `/orders` | Render static sample kitchen tickets and order history. |

The application does not yet submit orders, generate order IDs, or update kitchen statuses. The repository includes automated route, menu, and staff-form tests; database-backed tests use isolated temporary SQLite databases.

### Existing database schema upgrade

The staff form adds `description` and `icon` columns to `menu_items`. The migration at `migrations/add_menu_item_display_fields.py` is **not run automatically** and must not be replaced with `init-db`, which drops and recreates tables. After backing up the existing database and reviewing the migration, apply it explicitly with:

```powershell
python migrations/add_menu_item_display_fields.py instance/cafe.sqlite
```

The migration adds only missing columns, fills blank display fields for the existing sample menu items, and preserves other records and populated values.

## Getting started on Windows

Use Python 3.12 from PowerShell in the project folder. The virtual environment is local to this checkout and is excluded from Git.

```powershell
py -3.12 --version
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
flask --app app run --debug
```

Open <http://127.0.0.1:5000/> for the home page, <http://127.0.0.1:5000/menu> for the database-backed menu, and <http://127.0.0.1:5000/admin/menu/new> for the unauthenticated prototype staff form. An existing database needs the documented additive migration before menu pages or form submissions can use the new display columns. The current app's `app.run(debug=True)` also supports running it directly with `python app.py`.

To run the existing route tests, open another PowerShell terminal in the project folder, activate the environment, and run:

```powershell
python -m unittest discover -s tests -v
```

If PowerShell blocks activation, use `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`, then run the app with `.\.venv\Scripts\python.exe -m flask --app app run --debug` and tests with `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`.

## Project structure

Key Week 4 application files are organized as follows. Generated or ignored local files such as `.venv/`, `instance/`, and `__pycache__/` are not included.

```text
.
├── .gitignore
├── AI_INTERACTION_LOG.md
├── README.md
├── app.py
├── db.py
├── migrations/
│   └── add_menu_item_display_fields.py
├── requirements.txt
├── schema.sql
├── static/
│   └── style.css
├── templates/
│   ├── admin_menu_new.html
│   ├── ...
└── tests/
    └── test_app.py
```

## Academic milestones

- **Assignment 1.1 — Prototyping environment:** The repository began with the two-route Flask starter, templates, requirements, ignore rules, and route tests. The student should follow the instructor's evidence and disclosure requirements for any submitted work.
- **Assignment 1.2 — Café Calle Ocho:** This README documents the chosen concept, assumed problem statement, personas, target scope, exclusions, and user journeys. The current Week 4 prototype adds SQLite menu integration and staff menu-item creation; order submission and status updates remain planned.

---

**Repository:** [youneskouisaz-dot/egn475-cafe-kouis](https://github.com/youneskouisaz-dot/egn475-cafe-kouis)
