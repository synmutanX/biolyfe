from mongoengine import Document, IntField, LazyReferenceField, CASCADE

class Cart(Document):
    quantity = IntField(required=True)
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
        return f'<Cart {self.id}>'