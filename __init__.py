from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'gahan'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with app
    db.init_app(app)
    
    #Configure Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    #User loader function for Flask-Login
    from teachers import users
    @login_manager.user_loader
    def load_user(user_id):
        return users.query.get(int(user_id))
    
    from main import main
    app.register_blueprint(main)
    
    #Register blueprints
    from auth import loginbp
    app.register_blueprint(loginbp)
    
    from register import regbp
    app.register_blueprint(regbp) 
    
    from dasboard import studentbp
    app.register_blueprint(studentbp)

    return app