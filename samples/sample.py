from samples.model import User

User.create_table()
user = User(username='john_doe', email='john@example.com', age=10)
user.save()
