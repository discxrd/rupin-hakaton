from flask import Blueprint, render_template

home_bp = Blueprint("home_bp", __name__, template_folder="templates")

# если залогинен, то показывать пины, если нет - главную страницу
@home_bp.route("/", methods=["GET"])
def index():
    return render_template("/index.html")

@home_bp.route("/about", methods=["GET"])
def about():
    return render_template("/about.html")

@home_bp.route("/profile", methods=["GET"])
def profile():
    return render_template("/profile.html")