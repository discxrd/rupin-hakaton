from flask_login import UserMixin

from . import db
from . import login_manager

"""
Для Многие-ко-многим
"""

pin_tag = db.Table('pin_tag',
                    db.Column('pin_id', db.Integer, db.ForeignKey('pin.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                    )
#user_user = db.Table('user_user',
#                    db.Column('subscription_id', db.Integer, db.ForeignKey('user.id')),
#                    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
#                    )

"""
Модели пользователя
"""
@login_manager.user_loader
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nickname = db.Column(db.String(32), index=True, unique=True)

    email = db.Column(db.String(120), index=True, unique=True)
    avatar = db.Column(db.String(256))

    name = db.Column(db.String(64))

    password_hash = db.Column(db.String(128))

    created_pins = db.relationship('Pin', backref='user')
    saved_pins = db.relationship('SavedPin', backref='user')
    collections = db.relationship('Collection', backref='user')
    #subscriptions = db.relationship('User', secondary=user_user, backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.username) 

"""
Модели пинов
"""    

class Pin(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.Text)
    image_uri = db.Column(db.String(120))
    
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    comments = db.relationship('Comment', backref='pin')
    tags = db.relationship('Tag', secondary=pin_tag, backref='pin')
    
    def __repr__(self):
        return '<Pin {}>'.format(self.title)

class SavedPin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    main_pin_id = db.Column(db.Integer, db.ForeignKey("pin.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def __repr__(self):
        return '<SavedPin {}>'.format(self.pin_id)

class CollectedPin(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    collection_id = db.Column(db.Integer, db.ForeignKey("collection.id"))
    pin_id = db.Column(db.Integer, db.ForeignKey("pin.id"))

    def __repr__(self):
        return '<CollectedPin {}>'.format(self.collection_id) 

"""
Модель комментариев
"""

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    content = db.Column(db.Text)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    pin_id = db.Column(db.Integer, db.ForeignKey('pin.id'))

    def __repr__(self):
        return '<Comment {}>'.format(self.name) 

"""
Модель коллекции
"""

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(60))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    pins = db.relationship('CollectedPin', backref='collection')
    
    def __repr__(self):
        return '<Collection {}>'.format(self.name) 

"""
Модель тэга
"""

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(60))
    
    def __repr__(self):
        return '<Tag {}>'.format(self.name) 
