# EGN475 Week 4 Assignment Answer Drafts

> These drafts are grounded in the current code and verified behavior. The exact instructor question wording was not present in the project files. Rewrite these in your own words before submission.

## 1. How does the Flask app use SQLite?

The database helper opens a SQLite connection when a request first needs it and stores that connection on Flask's `g` object, so routes in the same request can reuse it. The connection uses `sqlite3.Row`, which lets route code access selected columns by name, and enables foreign-key enforcement. A registered teardown function closes the request-scoped connection. The app's database path is `instance/cafe.sqlite`.

## 2. How are menu queries and new-item inserts parameterized?

The menu route selects available items from `menu_items`, ordered by name. The item-detail route uses `WHERE id = ?`, with the requested ID passed separately as a parameter. The staff form's `INSERT` also uses `?` placeholders for every submitted value. A test submitted SQL-looking text as an item name and confirmed it was stored as text while the menu table remained present.

## 3. How does the staff form validate and save a price?

The form trims the name and category and rejects blank values. It parses the submitted dollar amount with `Decimal`, rejects negative or invalid values and amounts that cannot be represented in whole cents, then saves the integer cents to SQLite. For example, a test submitted `$0.29` and verified that `price_cents` was `29`. On success, the route commits the insert and redirects to `/menu`.

## 4. What happens when an insert is not committed?

In a no-commit experiment, `test_uncommitted_insert_is_not_persisted_in_temporary_database` used only the test suite's isolated temporary SQLite database. It inserted a test row through a request-scoped connection without calling `commit()`, then left the Flask app context so the connection closed. A new SQLite connection found no matching row. This demonstrates that a transaction can be discarded when a connection closes without a commit; the live database was not involved.
