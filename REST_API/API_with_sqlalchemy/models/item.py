from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True) # auto increamenting
    name = db.Column(db.String(80), unique=True, nullable=False) # name should be maxi 80 characters, unique, and cannot be null
    price = db.Column(db.Float(precision=2), unique=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("store.id"), unique=False, nullable=False) # 1-to-many relationship 

    # to grab a store with id equal to store_id
    store = db.relationship("StoreModel", back_populates="item") # get object in class StoreModel; this is a nested object inside an object