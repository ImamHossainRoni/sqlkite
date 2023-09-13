from sqlkite.orm.db import Database
from sqlkite.orm.models.fields import CharField, IntegerField


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

    class Meta:
        table_name = ''

    @classmethod
    def create_table(cls):
        if hasattr(cls, 'Meta') and hasattr(cls.Meta, 'table_name') and cls.Meta.table_name:
            table_name = cls.Meta.table_name
        else:
            # Use the default table name based on the class name
            table_name = cls.__name__.lower()

        columns = [
            f"{field_name} {field.__class__.__name__}"
            for field_name, field in cls.__dict__.items()
            if isinstance(field, (CharField, IntegerField))
        ]

        query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {', '.join(columns)})"
        cls.db.execute(query)

    def __init__(self, **kwargs):
        self.id = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        fields = ', '.join([f"'{key}'" for key in vars(self).keys() if key != 'id'])
        values = ', '.join([f"'{value}'" for value in vars(self).values() if value and value != self.id])

        if hasattr(self, 'Meta') and hasattr(self.Meta, 'table_name') and self.Meta.table_name:
            table_name = self.Meta.table_name
        else:
            # Use the default table name based on the class name
            table_name = self.__class__.__name__.lower()

        query = f"INSERT INTO {table_name} ({fields}) VALUES ({values})"
        self.db.execute(query)
