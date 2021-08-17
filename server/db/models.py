# from typing_extensions import Required
from . import db

class TaxonNode(db.Document):
    tax_id = db.StringField(required=True,unique=True)
    name = db.StringField(required=True)
    has_files = db.BooleanField(default=False)
    description = db.StringField()
    lineage = db.ListField(db.StringField())
    children = db.ListField(db.LazyReferenceField('self', passthrough=True))

class TaxonFile(db.Document):
    taxon = db.ReferenceField(TaxonNode, required=True)
    type = db.StringField()
    name = db.StringField(required=True, unique=True)
    file = db.FileField(required=True)

##implementation of geneid model to temporally persist ouput files, removed by client delete request
class GeneIdResults(db.Document):
    jpg = db.FileField() 
    ps = db.FileField()
    output = db.StringField(required=True)