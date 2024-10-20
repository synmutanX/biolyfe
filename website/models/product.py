from mongoengine import Document, StringField, FloatField, IntField, BooleanField, DateTimeField, ReferenceField, CASCADE
from datetime import datetime

class Product(Document):
    product_name = StringField(max_length=100, required=True)
    current_price = FloatField(required=True)
    previous_price = FloatField(required=True)
    in_stock = IntField(required=True)
    product_picture = StringField(max_length=1000, required=True)
    flash_sale = BooleanField(default=False)
    date_added = DateTimeField(default=datetime.timezone.utc)

    carts = ReferenceField('Cart', reverse_delete_rule=CASCADE)
    orders = ReferenceField('Order', reverse_delete_rule=CASCADE)

    def __str__(self):
        return f'<Product {self.product_name}>'