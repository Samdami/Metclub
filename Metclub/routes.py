from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required

# from flask_share import Share
# from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
from .models import User
from .models import BlogPost
import qrcode
import io
import shortuuid

from . import app, db


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email.lower()).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("home"))
            else:
                flash("Password incorrect. Please try again.")
        else:
            flash("Email is not registered yet.")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        user = User.query.filter_by(email=email.lower()).first()
        if user:
            flash("Email already exists.")
        elif len(name) < 2:
            flash("Name must be greater than 1 character.")
        elif len(username) < 2:
            flash("Username must be greater than 1 character.")
        elif len(password) < 6:
            flash("Password must be at least 6 characters.")
        elif password != confirm_password:
            flash("Passwords don't match.")
        else:
            new_user = User(
                email=email.lower(),
                username=username,
                password=generate_password_hash(password, method="sha256"),
            )

            db.session.add(new_user)
            db.session.commit()

    return render_template("signup.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")
