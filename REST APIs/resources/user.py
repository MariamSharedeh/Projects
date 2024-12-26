
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token


from db import db
from schemas import UserSchema
from models import UserModel



blp = Blueprint("Users", "users", description="Operations on users")


@blp.route("/registre")
class UserRegistre(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        #usernamme ds post man aussi !
        if UserModel.query.filter(UserModel.username==user_data["username"]).first():
            abort(409, message = "A user with that username already exists in that store.")
        user = UserModel(
             username = user_data["username"],
             password=pbkdf2_sha256.hash(user_data["password"]), 
        )
        db.session.add(user)
        db.session.commit()        
        return {"message": "User created successfully.","id": user.id, "username": user.username}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
         user = UserModel.query.filter( 
             UserModel.username==user_data["username"]
         ).first()
         if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=str(user.id))
            return {"access_token": access_token}, 200

         abort(401, message="Invalid credentials.")
       


    

@blp.route("/users/user/<int:user_id>")
class User(MethodView):
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return {"id": user.id, "username": user.username}


    def delete(self, user_id):
        #int : ca fait ref au user ds la bdd !
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        #raise NotImplementedError("Deleting a store is not implementes.")
        return {"message": "user deleted"}, 200
