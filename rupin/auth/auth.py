from flask import Blueprint, render_template

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates")

@auth_bp.route("/sign_in", methods=["GET"])
def sign_in():
    return render_template("/sign_in.html")

@auth_bp.route("/sign_up", methods=["GET"])
def sign_up():
    return render_template("/sign_up.html")
