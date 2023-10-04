import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from db import stores
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>") # endpoint is the same for the methods below
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            return abort(404, message = "Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            return abort(404, message = "Store not found")
        


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        # avoid duplicate store names
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message="Store already exists.")

        # add new store to the database
        store_id = uuid.uuid4().hex
        new_store = {**store_data, "id": store_id}
        stores[store_id] = new_store

        return new_store
