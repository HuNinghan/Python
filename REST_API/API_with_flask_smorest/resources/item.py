import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from db import items
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on stores")



@blp.route("/store/<string:item_id>") # endpoint is the same for the methods below
class Item(MethodView):
    @blp.response(200, ItemSchema) # this is the main response, which will be returned through ItemSchema
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            return abort(404, message = "Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            return abort(404, message = "Item not found")
        
    @blp.arguments(ItemUpdateSchema) # the order of the decorators matters
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item =items[item_id]
            item |= item_data  # update the item dictionary
            return item
        except KeyError:
            abort(404, message = "Item not found")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True)) # a list will be created for the multiple returns
    def get(self):
        return items.values()
    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        # DATA VALIDATION
        # if the item is already in the items dictionary
        for item in items.value():
            if (item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]):
                abort(400, message=f"Item already exists.")

        # add item to the database
        item_id = uuid.uuid4().hex
        item = {**item_data, "id":item_id}
        items[item_id] = item

        return item