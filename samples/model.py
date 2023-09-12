from sqlkite.orm.models import Model


class User(Model):
    table_name = 'users'

    username = ''
    email = ''


