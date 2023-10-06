import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items")



@blp.route("/store/<string:item_id>") # endpoint is the same for the methods below
class Item(MethodView):
    @blp.response(200, ItemSchema) # this is the main response, which will be returned through ItemSchema
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
       
        item = ItemModel.query.get_or_404(item_id)
        # a technique to tell the user or developer that the function is not completely developed yet
        # raise NotImplementedError("Deleting an item is not implemented.")

        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}        
        
    @blp.arguments(ItemUpdateSchema) # the order of the decorators matters
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)

        # idenpotency - different action result in same result.
        if item: # if item exists, then update it
            item.price = item_data["price"]
            item.name = item_data["name"]
        else: # otherwise, create the item
            item = ItemModel(item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True)) # a list will be created for the multiple returns
    def get(self):
        return ItemModel.query.all()
    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit() # can add multiple things and commit in the end
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item