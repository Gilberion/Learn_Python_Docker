from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.model import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)

    def set_password(self, password):
	    self.password_hash = generate_password_hash(password)

    def check_password(self,  password):
	    return check_password_hash(self.password_hash, password)

    def __repr__(self):
	    return "<{}:{}>".format(self.id, self.username)
