from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "hello"
import controller.user_controller as user_controller
import controller.product_controller as product_controller
from controller import * 