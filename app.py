from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controller import app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()
