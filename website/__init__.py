# from flask import Flask, render_template
from flask import Flask
from flask_login import LoginManager
from mongoengine import connect
# from .models import Customer  # Assuming your models are already converted to MongoEngine
# import logging
# logging.basicConfig(level=logging.DEBUG)

# DB_NAME = 'my_mongo_db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Connect to MongoDB using MongoEngine
    connect(db='my_mongo_db', host='localhost', port=27017)

    # @app.errorhandler(404)
    # def page_not_found(error):
    #     return render_template('404.html')

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # logging.debug('Models imported')
    # Import models after initialization
    from .models import Customer, Cart, Product, Order

    # User loader for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return Customer.objects(id=user_id).first()  # MongoEngine query to find user by id

    # Register your blueprints (views, auth, admin)
    from .views import views
    from .auth import auth
    from .admin import admin

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')

    return app
