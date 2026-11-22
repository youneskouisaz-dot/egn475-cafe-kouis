import argparse
import sqlite3
from pathlib import Path


SAMPLE_ITEM_DISPLAY_DATA = (
    ("Cuban coffee with steamed milk.", "☕", "Café con Leche"),
    ("Roasted pork, ham, Swiss cheese, and pickles.", "🥪", "Cuban Sandwich"),
    ("Flaky pastry filled with sweet guava.", "🥟", "Guava Pastry"),
    ("Cuban espresso balanced with a touch of steamed milk.", "☕", "Cortadito"),
    ("Roast pork, ham, Swiss, and pickles on soft sweet bread.", "🥪", "Medianoche Sandwich"),
    ("A chilled mango milkshake blended until smooth.", "🥤", "Mango Batido"),
    ("Medium-roast coffee with cocoa and caramel notes.", "☕", "Morning Roast"),
    ("Herbed ricotta, seasonal greens, and lemon on sourdough.", "🍞", "Garden Toast"),
    ("Fresh orange, lemon, and sparkling water over ice.", "🍊", "Citrus Sparkler"),
)


def migrate(database_path):
    database_path = Path(database_path)
    if not database_path.is_file():
        raise FileNotFoundError(f"Database does not exist: {database_path}")

    database_uri = f"{database_path.resolve().as_uri()}?mode=rw"
    connection = sqlite3.connect(database_uri, uri=True)
    try:
        with connection:
            connection.execute("BEGIN IMMEDIATE")
            columns = {
                row[1]
                for row in connection.execute("PRAGMA table_info(menu_items)")
            }
            if not columns:
                raise RuntimeError("The database does not contain a menu_items table.")

            if "description" not in columns:
                connection.execute(
                    "ALTER TABLE menu_items "
                    "ADD COLUMN description TEXT NOT NULL DEFAULT ''"
                )
            if "icon" not in columns:
                connection.execute(
                    "ALTER TABLE menu_items "
                    "ADD COLUMN icon TEXT NOT NULL DEFAULT ''"
                )

            connection.executemany(
                """
                UPDATE menu_items
                SET description = CASE
                        WHEN description IS NULL OR description = '' THEN ?
                        ELSE description
                    END,
                    icon = CASE
                        WHEN icon IS NULL OR icon = '' THEN ?
                        ELSE icon
                    END
                WHERE name = ?
                """,
                SAMPLE_ITEM_DISPLAY_DATA,
            )
    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser(
        description="Add menu display fields to an existing Café Calle Ocho database."
    )
    parser.add_argument(
        "database",
        type=Path,
        help="Path to an existing SQLite database; this script never creates a database.",
    )
    args = parser.parse_args()
    migrate(args.database)
    print("Menu item display fields are ready.")


if __name__ == "__main__":
    main()
