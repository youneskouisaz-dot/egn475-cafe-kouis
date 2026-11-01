<div align="center">

# Café Calle Ocho

### A neighborhood café, a clearer path from order to pickup.

**An EGN475 educational Flask prototype concept for a Cuban café in Little Havana, Miami.**

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![GitHub repository](https://img.shields.io/badge/GitHub-public%20repository-181717?logo=github&logoColor=white)](https://github.com/youneskouisaz-dot/egn475-cafe-kouis)
[![Project status](https://img.shields.io/badge/Project%20status-prototype%20planning-9A5B32)](#academic-milestones)

</div>

> **Scope note:** The current application is the Assignment 1.1 Café Kouis starter with two working routes: `/` and `/about`. Café Calle Ocho is the Assignment 1.2 ordering-system concept described in this README. Ordering, kitchen workflow, customer history, and menu administration are planned—not implemented in the current app.

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

This repository is an **EGN475 educational project**, not a production ordering service. The current Flask code remains the small two-route starter described below; the ordering experience is future development.

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

These are the **must-have features for the planned prototype**. They are not present in the current two-route starter yet.

1. Browse the café menu.
2. Select menu items.
3. Place an order.
4. Show an order confirmation with an ID.
5. Display a kitchen order board.
6. Update order status through **Received → Preparing → Ready → Picked Up**.
7. Provide order history and basic menu administration.

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

The repository currently contains the Assignment 1.1 Flask starter. `app.py` creates a Flask application and defines:

| Route | Current behavior |
| --- | --- |
| `/` | Renders the existing home-page template. |
| `/about` | Renders the existing prototype information page. |

The current application does **not** yet provide a menu, cart, order submission, order IDs, kitchen board, status updates, order history, or menu administration. The feature list above describes intended future scope only. The repository includes four automated route tests for the current starter; they do not test ordering functionality.

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

Open <http://127.0.0.1:5000/> for the home page and <http://127.0.0.1:5000/about> for the about page. The current app's `app.run(debug=True)` also supports running it directly with `python app.py`.

To run the existing route tests, open another PowerShell terminal in the project folder, activate the environment, and run:

```powershell
python -m unittest discover -s tests -v
```

If PowerShell blocks activation, use `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`, then run the app with `.\.venv\Scripts\python.exe -m flask --app app run --debug` and tests with `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`.

## Project structure

This tree lists files and directories currently present on the repository's `main` branch; it does not include generated or ignored local files such as `.venv/` or `__pycache__/`.

```text
.
├── .gitignore
├── AI_INTERACTION_LOG.md
├── EGN475_W1A1_KouisYounes.pdf
├── Q_AND_A_DRAFTS.md
├── README.md
├── app.py
├── automated-test-output.txt
├── browser-about.png
├── browser-home.png
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   ├── about.html
│   └── index.html
└── tests/
    └── test_app.py
```

## Academic milestones

- **Assignment 1.1 — Prototyping environment:** The repository contains the two-route Flask starter, templates, requirements, ignore rules, and route tests. The project files and tests were verified in the Manus Ubuntu sandbox. The student should independently recreate and run the environment on the required Windows computer and follow the instructor's evidence and disclosure requirements.
- **Assignment 1.2 — Café Calle Ocho:** This README documents the chosen concept, assumed problem statement, personas, target scope, exclusions, and user journeys. The ordering workflow is a planned design scope; it should not be described as implemented until it has actually been built and tested.

---

**Repository:** [youneskouisaz-dot/egn475-cafe-kouis](https://github.com/youneskouisaz-dot/egn475-cafe-kouis)
