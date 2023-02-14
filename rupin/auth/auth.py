from flask import Blueprint, render_template

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates")

@auth_bp.route("/", methods=["GET"])
def sign_in():
    return render_template("/sign_in.html")

@auth_bp.route("/", methods=["GET"])
def sign_out():
    return render_template("/sign_up.html")