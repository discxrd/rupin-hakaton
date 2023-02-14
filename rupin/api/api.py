from flask import Blueprint, redirect, request, url_for
from flask_login import login_user, login_required, logout_user

from rupin.models import User
from rupin.helpers import check_password_hash
from rupin import db

api_bp = Blueprint("api_bp", __name__, template_folder="templates")

"""
API для профиля
"""
@api_bp.route("/api/v1/user/<user_id>", methods=["GET"])
def profile_get(user_id: str):
    pass

@login_required
@api_bp.route("/api/v1/user/<user_id>/subscribe", methods=["GET"])
def profile_subscribe(user_id: str):
    pass

@login_required
@api_bp.route("/api/v1/user/<user_id>/unsubscribe", methods=["GET"])
def profile_unsubscribe(user_id: str):
    pass

@login_required
@api_bp.route("/api/v1/user/<user_id>/settings", methods=["POST"])
def profile_edit_settings(user_id: str):
    pass

"""
API для входа
"""

@api_bp.route("/api/v1/sign_in", methods=["POST"])
def sign_in():
    email = request.form.get('email')
    password_hash = request.form.get('hash')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password_hash):
        #flash('Please check your login details and try again.')
        #return redirect(url_for('auth.login'))
        return "error"

    login_user(user, remember=True)
    pass

@api_bp.route("/api/v1/sign_up", methods=["POST"])
def sign_up():
    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).all()

    if user:
        return "error"
    
    new_user = User(email=data["email"], nickname=data["nickname"], password_hash=data["hash"])
    
    db.session.add(new_user)
    db.session.commit()

    return "POPA"

@login_required
@api_bp.route("/api/v1/sign_out", methods=["POST"])
def sign_out():
    logout_user()

    return redirect(url_for("home.index"))

"""
API для пинов
"""
@login_required
@api_bp.route("/api/v1/pin/<pin_id>/edit", methods=["POST"])
def pin_edit(pin_id: str):
    pass

@login_required
@api_bp.route("/api/v1/pin/<pin_id>/delete", methods=["POST"])
def pin_delete(pin_id: str):
    pass

@login_required
@api_bp.route("/api/v1/pin/<pin_id>/save", methods=["POST"])
def pin_save(pin_id: str):
    pass

@login_required
@api_bp.route("/api/v1/pin/new", methods=["POST"])
def pin_new():
    pass

'''
Лента рекомендаций
'''

@login_required
@api_bp.route("/api/v1/feed", methods=["POST"])
def feed():
    pass