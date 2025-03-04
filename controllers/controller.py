from flask import Blueprint, render_template
from models.order_list import orders

controller = Blueprint("controller", __name__)  # Create a Blueprint

@controller.route("/")
def index():
    return render_template("index.html", title="Home", orders=orders)

@controller.route("/orders/<int:index>")
def order(index):
    return render_template("orders.html", title="Orders", order=orders[index])
