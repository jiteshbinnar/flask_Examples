from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///store.db'
app.config['SECRET_KEY']='fe76f20ff3987e0a4b36c629'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login_form"
login_manager.login_message_category="info"
app.app_context().push()


from store import routing

