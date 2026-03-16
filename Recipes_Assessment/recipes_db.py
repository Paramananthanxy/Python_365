import sqlite3

DB_NAME = "recipes.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cuisine TEXT,
        title TEXT,
        rating REAL,
        prep_time INTEGER,
        cook_time INTEGER,
        total_time INTEGER,
        description TEXT,
        nutrients TEXT,
        serves TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("Table created successfully")