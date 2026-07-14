import sqlite3
from contextlib import contextmanager

DATABASE_NAME = "school.db"

@contextmanager
def get_connection():
    """Provides a transactional context manager for SQLite."""
    connection = sqlite3.connect(DATABASE_NAME)
    try:
        yield connection
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
