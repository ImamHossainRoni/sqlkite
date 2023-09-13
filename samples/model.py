from sqlkite.orm.models import Model
from sqlkite.orm.models.fields import CharField, IntegerField


class User(Model):
    table_name = 'users'

    username = CharField(max_length=50)
    email = CharField(max_length=100)
    age = IntegerField()


