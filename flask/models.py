from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy



# Create a class User
class User(db.Model):
    __tablename__ = "users"


id = db.Column(db.Integer, primary_key=True), ForeignKey("users.id")
name = db.Column(db.String, nullable=False)
email = db.Column(db.String, nullable=False)
password = db.Column(db.String, nullable=False)


def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password


def is_authenticated(self):
    return True


def is_active(self):
    return True


def is_anonymous(self):
    return False


def get_id(self):
    return unicode(self.id)


def __repr__(self):
    return '<name - {}>'.format(self.name)