from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user,login_required,logout_user, current_user
from teachers import users
from werkzeug.security import check_password_hash
import secrets
from __init__ import db

loginbp = Blueprint("auth",__name__)

@loginbp.route("/login", methods=["GET","POST"])
def login(): 
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = users.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            token = secrets.token_hex(32)
            user.session_token = token
            db.session.commit()

            login_user(user)
            return redirect(url_for("student.fetch"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

@loginbp.route('/logout', methods=["POST"])
@login_required
def logout():
    current_user.session_token = None
    db.session.commit()
    logout_user()
    return redirect(url_for('login.html'))