from db import db

class  UserModel(db.Model):
    __tablename__ = "users" 
    id = db.Column(db.Integer,primary_key = True)
    username =db.Column(db.String(30),nullable=False,unique=True )
    password = db.Column(db.String(300), nullable = False)
    age = db.Column(db.Integer, nullable=True)  # Nouvelle colonne