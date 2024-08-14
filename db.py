from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model (example: User)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home():
    return "Database connected successfully!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database file and tables
    app.run(debug=True)
