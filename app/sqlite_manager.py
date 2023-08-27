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


def check_user(contact_name, phone_value):
    connection = None
    cursor = None
    try:
        conn = sqlite3.connect("db_hw9.db")
        cur = conn.cursor()

        sql_check = """
        SELECT contact_name, phone_value FROM phones;
        """

        # Return all DB lines (List of Tuples):
        res = cur.execute(sql_check)
        db_content = res.fetchall()

        # usr = one Tuple at a Time
        # usr[0] or "elm in usr" = first cell of every Tuple

        for usr in db_content:
            print(f"Show next tuple: {usr}")
            if usr[0] == contact_name and usr[1] == phone_value:
                return True
        return False

    except sqlite3.Error as error:
        print(f"Error checking User: \n{error}\n")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def put_user_info(contact_name, phone_value):
    connection = None
    cursor = None
    try:
        connection = sqlite3.connect("db_hw9.db")
        cursor = connection.cursor()

        sql_put = """
        INSERT INTO phones (contact_name, phone_value)
        VALUES(?, ?)
        """

        cursor.execute(sql_put, (contact_name, phone_value))
        connection.commit()

    except sqlite3.Error as error:
        print(f"Error with DB connection: \n{error}\n")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


def del_user_info(contact_name, phone_value):
    connection = None
    cursor = None
    try:
        connection = sqlite3.connect("db_hw9.db")
        cursor = connection.cursor()

        sql_del = """
        DELETE FROM phones WHERE contact_name=? AND phone_value=?
        """

        cursor.execute(sql_del, (contact_name, phone_value))  # Pass both parameters
        connection.commit()

    except sqlite3.Error as error:
        print(f"Error with DB connection: \n{error}\n")

    finally:
        if cursor:  # Use 'cur' instead of 'cursor'
            cursor.close()

        if connection:  # Use 'conn' instead of 'connection'
            connection.close()


# def get_all_info(u_nickname, u_password):
# connection = None
# cursor = None
#     try:
#         conn = sqlite3.connect("db_hw9.db")
#         cur = conn.cursor()
#
#         sql = """
#             SELECT nickname, password, house, magic_item_level FROM users;
#         """
#
#         # Return all DB lines (List of Tuples):
#         res = cur.execute(sql)
#         all_user_info = res.fetchall()
#         print(f"db_content: {all_user_info}")
#
#         for tuple_line in all_user_info:
#             print(f"Tuple line: {tuple_line}")
#             if u_nickname and u_password in tuple_line:
#                 return tuple_line
#         raise Exception("DB Error")
#
#     except sqlite3.Error as error:
#         print(f"Error with DB connection: \n{error}\n")
#
#     finally:
#         if cursor:
#             cursor.close()
#
#         if connection:
#             connection.close()
#
