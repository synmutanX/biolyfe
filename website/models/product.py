from mongoengine import Document, StringField, FloatField, IntField, BooleanField, DateTimeField, LazyReferenceField, CASCADE
from datetime import datetime, timezone

class Product(Document):
    product_name = StringField(max_length=100, required=True)
    current_price = FloatField(required=True)
    previous_price = FloatField(required=True)
    in_stock = IntField(required=True)
    product_picture = StringField(max_length=1000, required=True)
    flash_sale = BooleanField(default=False)
    date_added = DateTimeField(default=timezone.utc)

    # carts = LazyReferenceField('Cart', reverse_delete_rule=CASCADE)
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
    
    def __str__(self):
        return f'<Product {self.product_name}>'