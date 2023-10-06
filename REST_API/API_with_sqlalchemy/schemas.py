from marshmallow import Schema, fields

# need to reflect class object and nested class object
class PlainItemSchema(Schema): 
    id = fields.Str(dump_only=True) # required fields are for both ends of responds and requests
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str() # all of them are not required as an input
    price = fields.Float()
    store_id = fields.Int()


class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


# Nested object
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)