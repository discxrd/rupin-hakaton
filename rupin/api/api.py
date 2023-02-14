from flask import Blueprint, request

from rupin.models import User
from rupin import db

api_bp = Blueprint("api_bp", __name__, template_folder="templates")

"""
API для профиля
"""
@api_bp.route("/api/v1/user/<user_id>", methods=["GET"])
def profile_get(user_id: str):
    pass

@api_bp.route("/api/v1/user/<user_id>/subscribe", methods=["GET"])
def profile_subscribe(user_id: str):
    pass

@api_bp.route("/api/v1/user/<user_id>/unsubscribe", methods=["GET"])
def profile_unsubscribe(user_id: str):
    pass

@api_bp.route("/api/v1/user/<user_id>/settings", methods=["POST"])
def profile_edit_settings(user_id: str):
    pass

"""
API для входа
"""

@api_bp.route("/api/v1/sign_in", methods=["POST"])
def sign_in():
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



@api_bp.route("/api/v1/sign_out", methods=["POST"])
def sign_out():
    pass

"""
API для пинов
"""

@api_bp.route("/api/v1/pin/<pin_id>/edit", methods=["POST"])
def pin_edit(pin_id: str):
    pass

@api_bp.route("/api/v1/pin/<pin_id>/delete", methods=["POST"])
def pin_delete(pin_id: str):
    pass

@api_bp.route("/api/v1/pin/<pin_id>/save", methods=["POST"])
def pin_save(pin_id: str):
    pass

@api_bp.route("/api/v1/pin/new", methods=["POST"])
def pin_new(pin_id: str):
    pass