"""
Module: db.py
Author: Imam Hossain Roni
Created: October 01, 2022

Description: 'A research and development initiative for crafting a Python-centric ORM'
"""


import sqlite3


class Database:
    """
    A class to represent a database.

    Args:
        db_name (str): The name of the database file.

    Methods:
        execute(query, params=None): Executes a query.
        fetch_all(query, params=None): Fetches all rows from a query.
        close(): Closes the database connection.
    """
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
