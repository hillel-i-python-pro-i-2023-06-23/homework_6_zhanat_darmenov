import sqlite3


def create_table():
    connection = None
    cursor = None
    try:
        connection = sqlite3.connect("db_hw9.db")
        cursor = connection.cursor()

        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='phones'")
        result = cursor.fetchone()

        # Create table if it doesn't exist
        if not result:
            cursor.execute(
                """CREATE TABLE phones
                                 (phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  contact_name TEXT NOT NULL UNIQUE,
                                  phone_value TEXT NOT NULL )"""
            )
            connection.commit()

    except sqlite3.Error as error:
        print(f"Error with DB connection: \n{error}\n")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Call the function to create the table
create_table()
