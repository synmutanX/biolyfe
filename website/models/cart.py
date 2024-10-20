from mongoengine import Document, IntField, ReferenceField, CASCADE

class Cart(Document):
    quantity = IntField(required=True)
    customer_link = ReferenceField('Customer', reverse_delete_rule=CASCADE)
    product_link = ReferenceField('Product', reverse_delete_rule=CASCADE)
    
    def __str__(self):
        return f'<Cart {self.id}>'