from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    nickname = db.Column(db.String(32), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)

    avatar = db.Column(db.String(256), index=True, unique=False, nullable=True)
    name = db.Column(db.String(64), index=True, unique=False, nullable=True)

    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 