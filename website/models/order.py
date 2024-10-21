from mongoengine import Document, IntField, FloatField, StringField, LazyReferenceField, CASCADE

class Order(Document):
    quantity = IntField(required=True)
    price = FloatField(required=True)
    status = StringField(max_length=100, required=True)
    payment_id = StringField(max_length=1000, required=True)

    # customer_link = LazyReferenceField('Customer', reverse_delete_rule=CASCADE)
    # Lazy import Customer saat dibutuhkan
    @property
    def customer(self):
        from .customer import Customer
        return LazyReferenceField(Customer, reverse_delete_rule=CASCADE)

    # product_link = LazyReferenceField('Product', reverse_delete_rule=CASCADE)
    # lazy import Product saat dibutuhkan
    @property
    def product(self):
        from .product import Product
        return LazyReferenceField(Product, reverse_delete_rule=CASCADE)

    def __str__(self):
        return f'<Order {self.id}>'