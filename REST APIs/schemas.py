from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str()  # Si tu souhaites inclure cet attribut

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    # le champ doit obligatoirement être présent dans les données d'entrée.
    name = fields.Str(required=True)

class PlainTagSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

class StoreSchema(PlainStoreSchema):
    # dump_only=True ----> inclus uniquement lors de la sérialisation (pour les données sortantes)
    # lambda ----> éviter les références circulaires entre les deux schémas, permet de résoudre les dépendances entre les schémas de manière dynamique.   
    items = fields.List(fields.Nested(lambda: PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(lambda: PlainTagSchema()), dump_only=True)

class ItemSchema(PlainItemSchema):
    # load_only=True ---->  charger des données entrantes
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(lambda: StoreSchema(), dump_only=True)

class TagSchema(PlainTagSchema):
    # load_only=True ---->  charger des données entrantes
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(),dump_only=True)
    items = fields.List(fields.Nested(PlainStoreSchema()), dump_only=True)


class TagandItem(TagSchema,ItemSchema ):
    # load_only=True ---->  charger des données entrantes
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)
    
class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)
    message = fields.Str()
    
