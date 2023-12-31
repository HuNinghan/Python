"""
This API could:
- create stores on a post request
- create items on a post request
- retrieve all stores and items on a get request
- retrieve a particular store on a get request
- get only items in a store on a get request
- update item information
- delete store or item

The data is stored in a python list.

To manually test api:
https://app.insomnia.rest/app/dashboard/organizations
"""

from flask import Flask, request
from db import items, stores
import uuid
from flask_smorest import abort

app = Flask(__name__)


@app.get("/store") # https//127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())}


# create stores on a post request
@app.post("/store")
def create_store():
    store_data = request.get_json()

    # DATA VALIDATION
    # make sure name element is in the request
    if "name" not in store_data:
        abort(400, message="Bad request. Ensure 'name' is included in the JSON payload.")

    # avoid duplicate store names
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message="Store already exists.")

    # add new store to the database
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store

    return new_store, 201


# create items on a post request, save it under the store in the stores dict
@app.post("/item")
def create_item():
    item_data = request.get_json()

    # DATA VALIDATION
    # if element of the item is missing
    if ("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
        abort(400, message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.")
    
    # if the item is already in the items dictionary
    for item in items.value():
        if (item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]):
            abort(400, message=f"Item already exists.")

    # add item to the database
    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    items[item_id] = item

    return item, 201


# get store name
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return abort(404, message = "Store not found")
    

@app.delete("/store/<string:store_id>")
def del_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        return abort(404, message = "Store not found")


# get item
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return abort(404, message = "Item not found")


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        return abort(404, message = "Item not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(400, message="Bad request. Ensure 'price', and 'name' are included in the JSON payload.")

    try:
        item =items[item_id]
        item |= item_data  # update the item dictionary
        return item
    except KeyError:
        abort(404, message = "Item not found")
    

@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


if __name__ == "__main__":
    app.run(debug=True)