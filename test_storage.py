#!/usr/bin/env python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json

obj_Base = BaseModel()
obj_Base.title = "place"
obj_Base2 = BaseModel()
obj_Base2.title = "Home"

db = FileStorage()
db.new(obj_Base)
db.new(obj_Base2)
"print(db.all())"
print("-------------------\n")
db.save()

db.reload()
print("reload before sd")
sd = json.dumps(db.all())
print("dictionary -> ", sd)
for key, value in db.items():
    obj1 = BaseModel(**value)
    print(db.obj1())
    print("\n")