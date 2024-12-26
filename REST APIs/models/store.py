from db import db

class  StoreModel(db.Model):
    __tablename__ = "stores" 

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80),unique=True, nullable=False)
    #delete indique que si un élément est supprimé du modèle parent (ici Store), les éléments associés (les ItemModel
    #delete-orphan un élément est retiré de la relation ( si tu dissocies un ItemModel de son Store), cet élément sera supprimé de la base de données
    #items = db.relationship("ItemModel",back_populates="store", lazy ="dynamic", cascade ="all, delete")
    items = db.relationship("ItemModel",back_populates="store", lazy ="dynamic")
    tags  =  db.relationship("TagModel",back_populates="store", lazy ="dynamic")
    # store = StoreModel.query.get(1)
    # print(store.tags)  # Lis


