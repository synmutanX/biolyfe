from mongoengine import Document, StringField, DateTimeField, ReferenceField, CASCADE
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Customer(Document, UserMixin):
    email = StringField(max_length=100, unique=True, required=True)
    username = StringField(max_length=100, required=True)
    password_hash = StringField(max_length=150, required=True)
    date_joined = DateTimeField(default=datetime.timezone.utc)

    cart_items = ReferenceField('Cart', reverse_delete_rule=CASCADE)
    orders = ReferenceField('Order', reverse_delete_rule=CASCADE)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password=password)

    def __str__(self):
        return f'<Customer {self.username}>'
