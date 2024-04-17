from app import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500))


with app.app_context():
    db.create_all()
