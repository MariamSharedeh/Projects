import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

from sqlalchemy.exc import SQLAlchemyError
#from db import items
from db import db
from models import ItemModel, TagModel
from schemas import ItemSchema, TagSchema, TagandItem

blp = Blueprint("tags", "tags", description="Operations on tags")

@blp.route("/item/<string:item_id>/tag/<string:tag_id>")
class ItemTagLink(MethodView):
    @blp.arguments(TagSchema)  
    @blp.response(201, TagSchema)
    def post(self, item_id, tag_id):
        # Vérifier si l'item et le tag existent
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)
        # Vérifier si le tag est déjà lié à cet item
        if tag in item.tags:
            abort(400, message="This tag is already linked to the item.")
        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message="Error linking tag to item: " + str(e))
        return tag

    @blp.response(204)
    def delete(self, item_id, tag_id):
        # Vérifier si l'item et le tag existent
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        # Vérifier si le tag est lié à cet item
        if tag not in item.tags:
            abort(400, message="This tag is not linked to the item.")
        item.tags.remove(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            #db.session.rollback()
            abort(500, message="Error unlinking tag from item: " + str(e))

        return "", 204
    


