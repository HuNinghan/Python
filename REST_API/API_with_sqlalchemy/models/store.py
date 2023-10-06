from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    # to grab an item(s) object with store_id euqal to id
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete") 
    # lazy="dynamic": will not fetch unless specifically told; to speed up the app; 
    # cascade="all": when delete parent object, children will be deleted as well