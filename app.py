from flask import Flask
from controllers.controller import controller  # Import the Blueprint

app = Flask(__name__)

app.register_blueprint(controller)  # Register the Blueprint

if __name__ == "__main__":
    app.run()
