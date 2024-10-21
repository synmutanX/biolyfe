from mongoengine import Document, StringField, DateTimeField, LazyReferenceField, CASCADE
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

class Customer(Document, UserMixin):
    email = StringField(max_length=100, unique=True, required=True)
    username = StringField(max_length=100, required=True)
    password_hash = StringField(max_length=150, required=True)
    date_joined = DateTimeField(default=timezone.utc)

    # cart_items = LazyReferenceField('Cart', reverse_delete_rule=CASCADE)
    # orders = LazyReferenceField('Order', reverse_delete_rule=CASCADE)
    # Lazy import Cart saat dibutuhkan
    @property
    def cart_items(self):
        from .cart import Cart
        return LazyReferenceField(Cart, reverse_delete_rule=CASCADE)

    # orders = LazyReferenceField('Order', reverse_delete_rule=CASCADE)
    # Lazy import Order saat dibutuhkan
    @property
    def orders(self):
        from .order import Order
        return LazyReferenceField(Order, reverse_delete_rule=CASCADE)

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
