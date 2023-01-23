from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    type = db.Column(db.Enum("customer","manager", name='type_types'), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"), nullable=False)
    # user = db.Column(db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    birthday = db.Column(db.Date(), unique=False, nullable=True)
    gender = db.Column(db.Enum("female","male", name='gender_types'), unique=False, nullable=True)
    subscription = db.Column(db.Boolean(), unique=False, nullable=True, default=False)
    address = db.Column(db.String(150), unique=False, nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'

    def serialize(self):
        return {    "id": self.id,
                    "user_id": self.user_id,
                    "user_email": self.user.email,
                    "name": self.name,
                    "birthday": self.birthday,
                    "gender": self.gender,
                    "subscription": self.subscription,
                    "address": self.address
               }

class Manager(db.Model):
    __tablename__ = "managers"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"), nullable=False)
    #user = db.Column(db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

    def serialize(self):
        return {    "id": self.id,
                    "user_id": self.user_id,
                    "user_email": self.user.email,
                    "name": self.name
               }

class Comercial_Place(db.Model):
    __tablename__ = "comercial_places"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"), nullable=False)
    user = db.relationship(User, backref="comercial_place")
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(150), unique=False, nullable=False)
    url = db.Column(db.String(150), unique=False, nullable=True)
    telf = db.Column(db.String(15), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    location = db.Column(db.String(120), unique=True, nullable=True)
    description = db.Column(db.String(120), unique=True, nullable=False)
    cambiador = db.Column(db.Boolean(), unique=False, default=False)
    trona = db.Column(db.Boolean(), unique=False, default=False)
    accessible_carrito = db.Column(db.Boolean(), unique=False, default=False)
    espacio_carrito = db.Column(db.Boolean(), unique=False, default=False)
    ascensor = db.Column(db.Boolean(), unique=False, default=False)
    productos_higiene = db.Column(db.Boolean(), unique=False, default=False)

    def __repr__(self):
        return f'<User {self.name}>'

    def serialize(self):
        return {    "id": self.id,
                    "user_id": self.user_id,
                    "name": self.name,
                    "address": self.address,
                    "url": self.url,
                    "telf": self.telf,
                    "email": self.email,
                    "location": self.location,
                    "description": self.description,
                    "cambiador": self.cambiador,
                    "trona": self.trona,
                    "accessible": self.accessible_carrito,
                    "espacio_carrito": self.espacio_carrito,
                    "ascensor": self.ascensor,
                    "productos_higiene": self.productos_higiene,
               }

class Rate_Customer(db.Model):
    __tablename__ = "rates_customers"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.ForeignKey("customers.id"), nullable=False)
    customer = db.Column(db.ForeignKey("customers.id"), nullable=False)
    comercial_place_id = db.Column(db.ForeignKey("comercial_places.id"), nullable=False)
    comercial_place = db.relationship('Comercial_Place', backref='rates_customers', lazy=True)
    rate = db.Column(db.Enum("1","2","3","4","5", name='rate_types'), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.customer_id}>'

    def serialize(self):
        return {    "id": self.id,
                    "customer_id": self.customer_id,
                    "customer_name": self.customer.name,
                    "comercial_Place_id": self.comercial_Place_id,
                    "comercial_place_name": self.comercial_place.name,
                    "rate": self.rate
               }

class Photo_Comercial_Place(db.Model):
    __tablename__ = "photos_comercial_place"
    id = db.Column(db.Integer, primary_key=True)
    comercial_place_id = db.Column(db.ForeignKey("comercial_places.id"), nullable=False)
    comercial_place = db.relationship('Comercial_Place', backref='photos_comercial_place', lazy=True)
    location = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.customer_id}>'

    def serialize(self):
        return {    "id": self.id,
                    "comercial_Place_id": self.comercial_Place_id,
                    "comercial_Place_name": self.comercial_Place.name,
                    "location": self.location
               }

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"), nullable=False)
    user = db.relationship('User', backref='comments', lazy=True)
    comercial_place_id = db.Column(db.ForeignKey("comercial_places.id"), nullable=False)
    comercial_place = db.relationship('Comercial_Place', backref='comments', lazy=True)
    comment_id = db.Column(db.ForeignKey("comments.id"), nullable=False)
    date = db.Column(db.DateTime(), unique=False, nullable=False)
    comment = db.Column(db.String(1000), unique=False, nullable=False)
    
    def __repr__(self):
        return f'<User {self.customer_id}>'

    def serialize(self):
        return {    "id": self.id,
                    "user_id": self.user_id,
                    "user_name": self.user.name,
                    "comercial_Place_id": self.comercial_Place_id,
                    "comercial_Place_name": self.comercial_Place.name,
                    "comment_id": self.comment_id,
                    "date": self.date,
                    "comment": self.comment
               }

class Photos_Comments(db.Model):
    __tablename__ = "photos_comments"
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.ForeignKey("comments.id"), nullable=False)
    location = db.Column(db.String(1000), unique=False, nullable=False)
    
    def __repr__(self):
        return f'<User {self.customer_id}>'

    def serialize(self):
        return {    "id": self.id,
                    "comment_id": self.comment_id,
                    "location": self.location
               }

class Favourit(db.Model):
    __tablename__ = "favorits"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.ForeignKey("customers.id"), nullable=False)
    customer = db.relationship('Customer', backref='favorits', lazy=True)
    comercial_place_id = db.Column(db.ForeignKey("comercial_places.id"), nullable=False)
    comercial_place = db.relationship('Comercial_Place', backref='favorits', lazy=True)
    state = db.Column(db.Boolean(), unique=False, nullable=False)
    created_at = db.Column(db.DateTime(), unique=False, nullable=False,default=datetime.datetime.now())
    
    def __repr__(self):
        return f'<User {self.customer_id}>'

    def serialize(self):
        return {    "id": self.id,
                    "customer_id": self.customer_id,
                    "customer_name": self.customer.name,
                    "comercial_place_id": self.comercial_place_id,
                    "comercial_place_name": self.comercial_place.name,
                    "state": self.state,
                    "created_at": self.created_at
               }