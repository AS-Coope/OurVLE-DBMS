from flask import Flask
# from flask_login import LoginManager
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Flask-Login login manager
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

from app import views