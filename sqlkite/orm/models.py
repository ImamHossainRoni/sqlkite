from sqlkite.orm.db import Database


class Model:
    """
    A base class for all models.

    Attributes:
        db (Database): The database object.
        table_name (str): The name of the table in the database.

    Methods:
        create_table(): Creates the table in the database if it does not exist.
        __init__(**kwargs): Initializes the model with the given keyword arguments.
        save(): Saves the model to the database.
    """

    db = Database('database.db')
    table_name = ''

    @classmethod
    def create_table(cls):
        if not hasattr(cls, 'table_name'):
            raise ValueError("Model must define a 'table_name' attribute.")

            # Define the columns explicitly
        columns = [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "username TEXT",
            "email TEXT"
            # Add more columns as needed
        ]

        query = f"CREATE TABLE IF NOT EXISTS {cls.table_name} ({', '.join(columns)})"
        cls.db.execute(query)

    def __init__(self, **kwargs):
        self.id = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = ', '.join([f"'{key}'" for key in vars(self).keys() if key != 'id'])
        values = ', '.join([f"'{value}'" for value in vars(self).values() if value and value != self.id])
        query = f"INSERT INTO {self.table_name} ({fields}) VALUES ({values})"
        self.db.execute(query)
