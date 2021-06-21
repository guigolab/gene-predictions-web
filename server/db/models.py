# from typing_extensions import Required
from . import db

class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)

class Species(db.Document):
    tax_id = db.StringField(required=True)
    name = db.StringField()

class NewickFormat(db.Document):
    nwk = db.StringField(required=True)
    name = db.StringField(required=True)

class TaxonNode(db.Document):
    tax_id = db.StringField(required=True,unique=True)
    name = db.StringField(required=True,unique=True)
    description = db.StringField()
    is_species = db.BooleanField(default=True)

class TaxonFile(db.Document):
    taxon = db.ReferenceField(TaxonNode, required=True)
    type = db.StringField()
    name = db.StringField(required=True, unique=True)
    file = db.FileField(required=True)

