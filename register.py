from flask import Blueprint,Flask, render_template, request, redirect, url_for
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from teachers import users
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db

regbp = Blueprint("register",__name__)

# Register route
@regbp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if users.query.filter_by(username=username).first():
            return render_template("register.html", error="Username already taken!")

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = users(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.login"))
    
    return render_template("register.html")
