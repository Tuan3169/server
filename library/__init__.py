from flask import Flask
from .extention import create_database
from .Acount.controll import account
from .User.control import user_blueprint
from .DiemDanh.control import diemdanh_blueprint

def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    
    create_database(app.config.get("DATABASE_URI"))
    app.register_blueprint(account)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(diemdanh_blueprint)
    return app