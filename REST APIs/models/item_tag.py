from db import db

class  Item_tag_Model(db.Model):
    __tablename__ = "item_tag" 
    id =  db.Column(db.Integer, primary_key= True)
    tag_id = db.Column(db.Integer,db.ForeignKey('tags.id'),primary_key = True)
    item_id = db.Column(db.Integer,db.ForeignKey('items.id'),primary_key = True)


    